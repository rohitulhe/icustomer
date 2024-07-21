import pandas as pd
import psycopg2

def load_data(db_url, **kwargs):
    ti = kwargs['ti']
    csv_file = ti.xcom_pull(task_ids='transform')  # path to the CSV file from XCom

    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Ensure that 'timestamp' column is of datetime type
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

    # Connect to PostgreSQL using the connection string
    conn = psycopg2.connect(db_url)
    cur = conn.cursor()

    # Create the table if it doesn't exist
    cur.execute("""
    CREATE TABLE IF NOT EXISTS interactions (
        interaction_id SERIAL PRIMARY KEY,
        user_id INTEGER,
        product_id INTEGER,
        action TEXT,
        timestamp TIMESTAMP,
        user_interaction_count INTEGER,
        product_interaction_count INTEGER,
        last_updated TIMESTAMP
    );
    """)

    # Retrieve the maximum last_updated timestamp from the database
    cur.execute("SELECT MAX(last_updated) FROM interactions")
    last_load_time = cur.fetchone()[0]

    if last_load_time is None:
        last_load_time = pd.Timestamp.min  # If no records, set to the earliest possible time

    # Filter new or updated records from the DataFrame
    new_records = df[df['timestamp'] > last_load_time]

    # Insert new or updated records into the table
    for index, row in new_records.iterrows():
        cur.execute("""
        INSERT INTO interactions (user_id, product_id, action, timestamp, user_interaction_count, product_interaction_count, last_updated)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (interaction_id) DO UPDATE
        SET user_id = EXCLUDED.user_id,
            product_id = EXCLUDED.product_id,
            action = EXCLUDED.action,
            timestamp = EXCLUDED.timestamp,
            user_interaction_count = EXCLUDED.user_interaction_count,
            product_interaction_count = EXCLUDED.product_interaction_count,
            last_updated = EXCLUDED.last_updated
        """, (row['user_id'], row['product_id'], row['action'], row['timestamp'],
              row['user_interaction_count'], row['product_interaction_count'],
              row['timestamp']))

    # Commit changes and close the connection
    conn.commit()
    cur.close()
    conn.close()

    print("Incremental data loaded successfully into PostgreSQL.")

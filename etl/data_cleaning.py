import pandas as pd

def clean_data(**kwargs):
    ti = kwargs['ti']
    csv_file = ti.xcom_pull(task_ids='ingest')
    df = pd.read_csv(csv_file)
    # Handle missing values
    df = df.dropna(subset=['interaction_id', 'user_id', 'product_id', 'action', 'timestamp'])

    # Convert timestamp to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

    # Drop rows with invalid timestamps
    df = df.dropna(subset=['timestamp'])

    cleaned_csv_file = '/tmp/cleaned_interaction.csv'
    df.to_csv(cleaned_csv_file, index=False)
    return cleaned_csv_file  #file path to be passed via XCom

from etl.data_ingestion import ingest_data
from etl.data_cleaning import clean_data
from etl.data_transformation import transform_data
from etl.data_loading import load_data


def main(csv_file, db_url):
    # Ingest data
    df = ingest_data(csv_file)
    print("Data read from CSV file")

    # Clean data
    df = clean_data(df)
    print("Data cleaned from CSV file")

    # Transform data
    df = transform_data(df)
    print("Data transformed from CSV file")

    # Load data
    load_data(df, db_url)
    print("ETL process completed successfully.")


if __name__ == "__main__":
    csv_file = 'data/interaction.csv'  # replace with your CSV file path
    db_url = 'postgresql://postgres:postgres@localhost:5432/icustomer'  # replace with your PostgreSQL URL
    main(csv_file, db_url)



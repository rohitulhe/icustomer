import pandas as pd

def ingest_data(csv_file, **kwargs):
    df = pd.read_csv(csv_file)
    processed_csv_file = '/tmp/processed_interaction.csv'
    df.to_csv(processed_csv_file, index=False)
    return processed_csv_file  # file path to be passed via XCo

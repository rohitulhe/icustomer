import pandas as pd

def transform_data(**kwargs):
    ti = kwargs['ti']
    csv_file = ti.xcom_pull(task_ids='clean')
    df = pd.read_csv(csv_file)
    # Calculate interaction count per user and product
    interaction_count_per_user = df.groupby('user_id').size().reset_index(name='user_interaction_count')
    interaction_count_per_product = df.groupby('product_id').size().reset_index(name='product_interaction_count')

    # Merge interaction counts back to the original dataframe
    df = df.merge(interaction_count_per_user, on='user_id', how='left')
    df = df.merge(interaction_count_per_product, on='product_id', how='left')
    transformed_csv_file = '/tmp/transformed_interaction.csv'
    df.to_csv(transformed_csv_file, index=False)
    return transformed_csv_file  # Return the file path to be passed via XCom

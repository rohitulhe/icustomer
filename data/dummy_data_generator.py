import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Parameters
num_rows = 2000

# Helper functions
def random_date(start, end):
    """Generate a random datetime between `start` and `end`"""
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())))

# Date range for timestamp
start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 12, 31)

# Generate data
data = {
    'interaction_id': range(1, num_rows + 1),
    'user_id': np.random.randint(1, 101, num_rows),  # user_id between 1 and 100
    'product_id': np.random.randint(1, 51, num_rows),  # product_id between 1 and 50
    'action': np.random.choice(['view', 'click', 'purchase', 'like'], num_rows),
    'timestamp': [random_date(start_date, end_date) for _ in range(num_rows)]
}


# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('interaction.csv', index=False)

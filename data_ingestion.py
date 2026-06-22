import pandas as pd
import os

data_path = "data/raw"

files = [f for f in os.listdir(data_path) if f.endswith(".csv")]

for file in files:
    print("\n" + "="*60)
    print(f"FILE: {file}")
    print("="*60)

    df = pd.read_csv(os.path.join(data_path, file))

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())
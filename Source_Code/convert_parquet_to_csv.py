import pandas as pd
import fastparquet
parquet_path = "/content/drive/MyDrive/DPL 2025/artifacts/<file_name>"
csv_path = "/content/drive/MyDrive/DPL 2025/artifacts/<file_name>"
df = pd.read_parquet(parquet_path, engine='fastparquet')
df.to_csv(csv_path, index=False)
print(f"Saved CSV file to {csv_path}")


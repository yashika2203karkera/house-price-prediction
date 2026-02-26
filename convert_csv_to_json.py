import pandas as pd

# Load CSV file
df = pd.read_csv("house_prices.csv")

# Optional: Remove missing values
df = df.dropna()

# Convert to JSON
df.to_json("housing.json", orient="records", indent=4)

print("CSV converted to JSON successfully!")
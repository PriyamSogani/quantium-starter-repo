import pandas as pd
import glob

# Load all CSV files from the data folder
files = glob.glob('data/*.csv')
df = pd.concat((pd.read_csv(f) for f in files), ignore_index=True)

# Filter for Pink Morsels
df = df[df['product'].str.lower() == 'pink morsel']

# Remove dollar sign and convert price to float
df['price'] = df['price'].str.replace('$', '', regex=False).astype(float)

# Calculate sales
df['sales'] = df['quantity'] * df['price']

# Select required columns and save to a new CSV
df[['sales', 'date', 'region']].to_csv('formatted_sales_data.csv', index=False)
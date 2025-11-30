import pandas as pd


import os
os.makedirs('output/tables', exist_ok=True)
os.makedirs('output/plots', exist_ok=True)



file_path = "/Users/jonathanherrera/Desktop/CarbonMarketSimulation/data/nc-allowance_prices.csv"

data = pd.read_csv(file_path)

print(data.head())
print(data.columns)

def clean_cca_data(input_path,output_path):

    df = pd.read_csv(input_path)

    print("\n--- RAW DATA ---")
    print(df.head())
    print(df.dtypes)

    df = df.rename(columns={
            'Quarter Year': 'QuarterYear',
            'Current Auction Settlement Price': 'SettlementPrice',
            'Auction Reserve Price': 'ReservePrice'
        })

        # Fix quarter format
    df['QuarterYear'] = df['QuarterYear'].str.replace(
            r'(Q\d)\s+(\d{4})', r'\2\1', regex=True
        )

        # Fix prices BEFORE numeric conversion
    df['SettlementPrice'] = df['SettlementPrice'].str.replace(r'[$, ]', '', regex=True)
    df['ReservePrice'] = df['ReservePrice'].str.replace(r'[$, ]', '', regex=True)

    print("\n--- AFTER CLEANING PRICE STRINGS ---")
    print(df[['SettlementPrice', 'ReservePrice']].head())

        # Convert to numeric
    df['SettlementPrice'] = pd.to_numeric(df['SettlementPrice'], errors='coerce')
    df['ReservePrice'] = pd.to_numeric(df['ReservePrice'], errors='coerce')

    print("\n--- AFTER NUMERIC CONVERSION ---")
    print(df[['SettlementPrice', 'ReservePrice']].head())

        # Drop rows with missing prices
    df_before_drop = len(df)
    df = df.dropna(subset=['SettlementPrice'])
    print(f"\nDropped rows: {df_before_drop - len(df)}")

    print("\n--- AFTER DROPPING NA ---")
    print(df.head())

        # Convert QuarterYear → Date
    df['Date'] = pd.PeriodIndex(df['QuarterYear'], freq='Q').to_timestamp()

        # Sort
    df = df.sort_values('Date')

        # Save
    cleaned = df[['Date', 'SettlementPrice', 'ReservePrice']]
    cleaned.to_csv(output_path, index=False)
    print("\nSaved cleaned data.")
    

if __name__ == '__main__':
    clean_cca_data("/Users/jonathanherrera/Desktop/CarbonMarketSimulation/data/nc-allowance_prices.csv","/Users/jonathanherrera/Desktop/CarbonMarketSimulation/data/cca_prices_clean.csv")

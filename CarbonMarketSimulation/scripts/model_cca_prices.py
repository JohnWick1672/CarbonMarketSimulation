import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


import os
os.makedirs('output/tables', exist_ok=True)
os.makedirs('output/plots', exist_ok=True)


def load_data(path = "/Users/jonathanherrera/Desktop/CarbonMarketSimulation/data/cca_prices_clean.csv"):
    df = pd.read_csv(path)
    return df

df = load_data()
print(df.head())

#Summary of data set

print('Average Settlement Price: ',round(df['SettlementPrice'].mean(),2))
print('Average Reserve Price: ',round(df['ReservePrice'].mean(),2))
print('Earliest date: ',df['Date'].min())
print('Latest date: ', df['Date'].max())

max_price = df['SettlementPrice'].max()
min_price = df['SettlementPrice'].min()

max_date = df[df['SettlementPrice'] == max_price]['Date'].values[0]
min_date = df[df['SettlementPrice'] == min_price]['Date'].values[0]

print('Highest Settlement Price: $', round(max_price),  'on ', max_date)
print('Lowest Settlement Price: $', round(min_price), 'on ', min_date)

#Percent change between quarters
df['PercentChange'] = round(df['SettlementPrice'].pct_change(),3) * 100

# rolling average
df['RollingAvg'] = df['SettlementPrice'].rolling(4).mean()

#Visualize trends
plt.figure(figsize=(10,6))
plt.plot(df['Date'], df['SettlementPrice'], label='Settlement Price')
plt.plot(df['Date'], df['RollingAvg'], color='red', label='4 quarter Rolling Avg')
plt.xlabel('Date')
plt.xticks(df['Date'][::4], rotation=45) 
plt.ylabel('Settlement Price ($)')
plt.title('CCA Settlement Price Over Time')
plt.grid(True)
plt.legend()

# Save plot to output/plots
plt.savefig('output/plots/settlement_price_trends.png', bbox_inches='tight')
plt.close()

# Save dataframe with rolling avg and percent change to tables folder
df.to_csv('output/tables/cca_prices_with_rolling.csv', index=False)

#save data 
print(df.head())
df.to_csv('/Users/jonathanherrera/Desktop/CarbonMarketSimulation/data/cca_prices_clean.csv',index = False)




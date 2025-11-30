import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
from statsmodels.tsa.holtwinters import ExponentialSmoothing

import os
os.makedirs('output/tables', exist_ok=True)
os.makedirs('output/plots', exist_ok=True)

#Load Table
df = pd.read_csv('/Users/jonathanherrera/Desktop/CarbonMarketSimulation/data/cca_prices_clean.csv')

#To datetime
df['Date'] = pd.to_datetime(df['Date'])

#Setting date as the index
df.set_index('Date', inplace = True)

# column to be forecasted
col = df['SettlementPrice']

#ARIMA model
model = ARIMA(col, order = (1,1,1))

#fitting the model
result = model.fit()

#output
print(result.summary())

#FORECASTING values for table

n_periods = 4

forecast_col = result.get_forecast(steps = n_periods)
forecast_vals = forecast_col.predicted_mean
conf_interval = forecast_col.conf_int()
last_date = df.index.max()
forecast_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=n_periods, freq='QS-OCT')

#Table of Forecast
forecast_table = pd.DataFrame({'Date': forecast_dates,
    'Forecast': forecast_vals,
    'Lower_CI': conf_interval.iloc[:, 0],
    'Upper_CI': conf_interval.iloc[:, 1]
})

#SAVING OUTPUTS
# Save forecast table
forecast_table.to_csv('output/tables/forecast_cca_prices.csv', index=False)

#PLOTTING FORECAST
forecast_plot_dates = pd.concat([pd.Series([df.index.max()]), forecast_table['Date']])
forecast_plot_vals = pd.concat([pd.Series([df['SettlementPrice'].iloc[-1]]), forecast_table['Forecast']])
forecast_plot_lower = pd.concat([pd.Series([df['SettlementPrice'].iloc[-1]]), forecast_table['Lower_CI']])
forecast_plot_upper = pd.concat([pd.Series([df['SettlementPrice'].iloc[-1]]), forecast_table['Upper_CI']])

plt.figure(figsize=(10,6))
# Historical line
plt.plot(df.index.values, df['SettlementPrice'].values, label='Historical', color='blue')
# Forecast line
plt.plot(forecast_plot_dates.values, forecast_plot_vals.values, label='Forecast', color='red')
# Confidence interval
plt.fill_between(forecast_plot_dates.values,
                 forecast_plot_lower.values,
                 forecast_plot_upper.values,
                 color='pink', alpha=0.3)
plt.xlabel('Date')
plt.ylabel('Settlement Price ($)')
plt.title('CCA Settlement Price Forecast')
plt.legend()
plt.grid(True)
plt.savefig('output/plots/forecast_cca_prices.png', bbox_inches='tight')  # save after plotting
plt.show()
plt.close()

#MODEL EVALUATION AND RESIDUALS
train = col[:-4]
test = col[-4:]

model_train = ARIMA(train,order = (1,1,1))
result_train = model_train.fit()

forecast_test = result_train.forecast(steps = len(test))
rmse = np.sqrt(mean_squared_error(test,forecast_test))
mae = mean_absolute_error(test,forecast_test)

print(f"RMSE: {rmse}, MAE: {mae}")

residuals = result_train.resid
plt.figure(figsize=(10,4))
plt.plot(residuals)
plt.axhline(0, color='red', linestyle='--')
plt.title("Residuals of ARIMA Model")
plt.savefig('output/plots/arima_residuals.png', bbox_inches='tight')  # save before show
plt.show()
plt.close()

#------------------------------------------------------------
#HOLT-WINTERS MODEL
hw_model = ExponentialSmoothing(train, trend = 'add', seasonal = None)
hw_result = hw_model.fit()

hw_forecast = hw_result.forecast(steps=len(test))
hw_rmse = np.sqrt(mean_squared_error(test, hw_forecast))
hw_mae = mean_absolute_error(test, hw_forecast)
print(f"Holt-Winters RMSE: {hw_rmse}, MAE: {hw_mae}")



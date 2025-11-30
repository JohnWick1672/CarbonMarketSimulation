# CarbonMarketSimulation
A time series forecasting project analyzing California Carbon Allowance (CCA) auction settlement prices.

## Project Overview
I started this project because I have always liked working at the intersection of data and science. In the past, I worked on light pollution research, so when I came across carbon markets and read about Braeswood Carbon's work, I wanted to understand how these allowance prices actually behave. I took the historical CCA settlement data and treated it like any other system I would study in physics: clean it, visualize it, and try to model the behavior simply.

I built two forecasting models, ARIMA and Holt-Winters, to see whether short-term movements in this market could be captured with basic time series tools. What stood out to me was how smooth the price series was. I expected something closer to a typical commodity, but the trend lined up with how the emissions cap tightens over time. That taught me that policy-driven markets follow their own structure, and understanding that structure helps with forecasting.

This project helped me connect my physics background with real environmental data, and it gave me a clearer picture of how carbon markets evolve and how to approach them as a quantitative problem.

## What this Repository Contains
- Cleaned California Carbon Allowance market data  
- Python scripts for exploration, modeling, and evaluation  
- ARIMA and Holt-Winters forecasting models  
- Plots and tables generated from the analysis  
- A complete workflow from loading the data to producing forecasts  

## How to Run the Project

Install required packages:
pandas
numpy
matplotlib
statsmodels
scikit-learn

## Project Structure
```
CarbonMarketSimulation/
│
├── data/
│   ├── cca_prices_clean.csv
│   └── nc-allowance_prices.csv
│
├── scripts/
│   ├── data_cleaning.py
│   ├── forcast_cca_prices.py
│   └── model_cca_prices.py
│
└── output/
    ├── plots/
    │   ├── arima_residuals.png
    │   ├── forecast_cca_prices.png
    │   └── settlement_price_trends.png
    └── tables/
        ├── cca_prices_with_rolling.csv
        └── forecast_cca_prices.csv
```        
## Key Insights from the Analysis
- The CCA price series shows a steady upward trend that reflects how the emissions cap tightens over time  
- The market behaves more smoothly than typical commodities, which makes sense for a policy-driven system  
- ARIMA captures short-term movements reasonably well  
- Evaluation metrics such as RMSE, MAE, and residual checks help reveal where simple models fall short  

## Final Notes
This project is part of my interest in environmental markets and in applying data-driven tools to systems shaped by scientific and policy signals. I am open to discussing the work or exploring related topics.

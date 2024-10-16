# QuantStock: Performance Analytics and Benchmarking System
## Introduction
The QuantStock Performance Analytics and Benchmarking System is designed to help users analyze the historical performance of individual stocks in the S&P 500 index. By leveraging historical price data, this system computes key financial metrics such as Sharpe Ratio, Volatility, and Cumulative Returns, allowing users to evaluate stock performance relative to a benchmark. The system also automates the generation of detailed performance reports in PDF format.

## Project Structure
The project is structured into several directories to organize the dataset, Jupyter notebook, scripts, and generated reports.


```bash
QuantStock_Project/
│
├── data/                     
│   ├── all_stocks_5yr.csv         # CSV file with S&P 500 stock data
│   └── calculated_metrics.csv  # Calculated metrics saved from the Jupyter notebook
│
├── notebooks/
│   └── QuantStock_Analysis.ipynb  # Jupyter notebook for data analysis
│
├── reports/                  
│   └── AAPL_performance_report.pdf
│
├── scripts/
│   └── generate_report.py     # Python script to generate the performance report
│
├── README.md                  # Project documentation
└── requirements.txt           # Dependencies for the project
```


## Features
- Daily Stock Return Calculations: Automatically computes daily percentage changes in stock prices.
- Benchmark Comparison: Allows for comparing individual stock performance to a market benchmark (S&P 500 index).
- Cumulative Returns: Calculates cumulative returns for both the stock and the benchmark over time.
- Financial Metrics: Computes important financial metrics like Sharpe Ratio and Volatility.
- Automated PDF Report Generation: Generates professional PDF performance reports with key metrics and insights.
## Getting Started
### Prerequisites
Before you can run this project, ensure that you have the following installed:

- Python 3.x
- Required Python libraries (can be installed using requirements.txt)

### Installation
1. Clone the repository or download the project files.

2. Navigate to the project directory:


`cd QuantStock_Project`

3. Install the required dependencies:

`pip install -r requirements.txt`

## How to Run the Project
### Step 1: Data Analysis in Jupyter Notebook
1. Open the Jupyter Notebook: Navigate to the notebooks/ directory and open the QuantStock_Analysis.ipynb file using Jupyter Notebook.

`jupyter notebook notebooks/QuantStock_Analysis.ipynb`

2. Run the analysis: Execute all the cells to:

- Filter stock data for analysis.
- Calculate daily returns, Sharpe Ratio, and Volatility.
- Save the calculated metrics to a CSV file (calculated_metrics.csv).

### Step 2: Generate PDF Report

1. Run the generate_report.py script: This script will read the saved metrics from the CSV file and generate a PDF report for the selected stock.

`python scripts/generate_report.py`

2. Find the generated report: The PDF report will be saved in the reports/ directory with a filename based on the stock name (e.g., AAPL_performance_report.pdf).

## Customization
- Analyzing Different Stocks: You can change the stock symbol in the Jupyter Notebook to analyze any stock in the S&P 500 dataset. After analyzing a different stock, re-run the  Python script to generate a new report for that stock.

- Adjusting the Benchmark: By default, the system uses the mean of S&P 500 stocks as the benchmark. You can modify this to any custom benchmark of your choice by editing the code in the Jupyter Notebook.

## Dependencies
The project requires the following Python libraries, which are listed in the requirements.txt file:

- pandas
- numpy
- matplotlib
- fpdf
To install all dependencies, run:

`pip install -r requirements.txt`


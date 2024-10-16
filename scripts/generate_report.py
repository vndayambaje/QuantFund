#!/usr/bin/env python3

import pandas as pd
from fpdf import FPDF
from datetime import datetime

# Load the calculated values from the CSV file
metrics_df = pd.read_csv('../data/calculated_metrics.csv')

# Extract the values from the DataFrame
stock_name = metrics_df['stock_name'][0]
sharpe_ratio = metrics_df['sharpe_ratio'][0]
volatility = metrics_df['volatility'][0]
benchmark_sharpe = metrics_df['benchmark_sharpe'][0]
benchmark_volatility = metrics_df['benchmark_volatility'][0]

# Create the PDF report
def generate_report(stock_name, sharpe_ratio, volatility, benchmark_sharpe, benchmark_volatility):
    pdf = FPDF()
    pdf.add_page()

    # Report title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt=f"{stock_name} Performance Report", ln=True, align="C")

    # Report details
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Stock: {stock_name}", ln=True)
    pdf.cell(200, 10, txt=f"Date: {datetime.today().strftime('%Y-%m-%d')}", ln=True)
    pdf.cell(200, 10, txt=f"Sharpe Ratio (Stock): {sharpe_ratio:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Volatility (Stock): {volatility:.2%}", ln=True)
    pdf.cell(200, 10, txt=f"Sharpe Ratio (Benchmark): {benchmark_sharpe:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Volatility (Benchmark): {benchmark_volatility:.2%}", ln=True)

    # Dynamically create the filename
    file_name = f"../reports/{stock_name}_performance_report.pdf"
    
    # Save the PDF with the dynamic filename
    pdf.output(file_name)

    print(f"Report saved as: {file_name}")

# Automatically generate the report with the values loaded from the CSV
generate_report(stock_name, sharpe_ratio, volatility, benchmark_sharpe, benchmark_volatility)




# Stock Analytics Dashboard

Hello! This is a fun, interactive web application for analyzing stock correlations, beta coefficients, and historical price charts. This is built with a Python Flask backend and a JavaScript frontend using Chart.js for visualizations.

## Features

- Fetch and visualize correlation matrix of user-selected stocks
- Calculate beta coefficients relative to S&P 500 benchmark
- Display interactive historical price charts with customizable stock selection
- Responsive and user-friendly interface with dynamic heatmaps and dropdown menus

## Technologies Used

- **Backend:** Python, Flask, yfinance (Yahoo Finance API wrapper), pandas
- **Frontend:** HTML, CSS, JavaScript, Chart.js
- **Data Visualization:** Chart.js matrix and line charts
- **Deployment:** Flask development server

## Getting Started

### Prerequisites

- Python 3.7+
- pip package manager

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/aryap1206/stock-analytics-dashboard.git
   cd stock-analytics-dashboard

2. Install packages:
   ```bash
   pip install -r requirements.txt

4. Run Flask app
   ```bash
   python app.py

5. Open your browser at [text](http://127.0.0.1:5000)

### Usage
- Enter stock tickers only separated by commas (ex:AAPL,GOOG,NVDA)
- View the heatmap displaying correlations based on 6 months of data
- Analyze beta coefficients representing volatity of entered stocks
- Select stock from dropdown to view an interactive 6 month price chart with daily prices


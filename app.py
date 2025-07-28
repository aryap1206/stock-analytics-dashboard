from flask import Flask, request, jsonify, render_template
import yfinance as yf
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/correlation")
def get_correlation():
    tickers = request.args.get("tickers", "AAPL,MSFT").upper().split(",")
    
    data = yf.download(tickers, period="6mo", auto_adjust=True)["Close"].dropna()
    
    returns = data.pct_change().dropna()
    
    corr = returns.corr()
    
    return jsonify(corr.round(4).to_dict())

@app.route("/api/prices")
def get_prices():
    tickers = request.args.get("tickers", "AAPL,MSFT").upper().split(",")
    
    price_data = {}
    
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="2d")  
            
            if len(hist) >= 2:
                current_price = hist['Close'].iloc[-1]
                previous_price = hist['Close'].iloc[-2]
                change_pct = ((current_price - previous_price) / previous_price) * 100
                
                price_data[ticker] = {
                    "price": round(current_price, 2),
                    "change": round(change_pct, 2)
                }
            else:
                price_data[ticker] = {
                    "price": "N/A",
                    "change": "N/A"
                }
        except:
            price_data[ticker] = {
                "price": "N/A", 
                "change": "N/A"
            }
    
    return jsonify(price_data)

@app.route("/api/beta")
def get_beta():
    tickers = request.args.get("tickers","AAPL,MSFT").upper().split(",")
    sp = request.args.get("benchmark","^GSPC").upper()

    downloads = tickers + [sp]
    
    try:
        data = yf.download(downloads, period = "6mo", auto_adjust=True)["Close"].dropna()
        returns = data.pct_change().dropna()
        
        print("Returns columns:", returns.columns.tolist())
        benchmark = returns[sp]

        betas = {}

        for tick in tickers:
            if tick in returns:
                cov = returns[tick].cov(benchmark)
                var = benchmark.var()
                beta = cov / var if var != 0 else None
                betas[tick] = round(beta,4) if beta is not None else "N/A"
            else:
                betas[tick] = "N/A"

        return jsonify(betas)      
    except Exception as e:
        return jsonify({"error":str(e)})     
    
@app.route("/api/chart")
def get_chart_data():
    ticker = request.args.get("ticker", "AAPL").upper()
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="6mo")
        dates = hist.index.strftime("%m/%d/%y").tolist()
        prices = hist["Close"].tolist()
        return jsonify({"dates" : dates, "prices" : prices})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)

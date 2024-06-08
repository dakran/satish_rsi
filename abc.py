import yfinance as yf
import pandas as pd

def calculate_rsi(data, window=14):
    delta = data['Close'].diff()  # Use the correct column name for the closing price
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    # EMA
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()

    # SMA
    #avg_gain = gain.rolling(window=window).mean()
    #avg_loss = loss.rolling(window=window).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi

# Example usage
stock_symbols = ['AAPL', 'MSFT', 'GOOGL']  # Example: Apple, Microsoft, Google

# Create an empty DataFrame to store RSI values for each stock
rsi_df = pd.DataFrame()

# Fetch daily stock data for each stock
for symbol in stock_symbols:
    stock_data = yf.download(symbol, start='2024-01-01', end='2024-06-08', interval='1d')  # Adjust date range as needed

    # Calculate RSI for daily data
    stock_data['RSI'] = calculate_rsi(stock_data)

    # Add RSI values to the DataFrame
    rsi_df[symbol] = stock_data['RSI']

# Store RSI values in a CSV file
rsi_df.to_csv("daily_rsi.csv")
print("Daily RSI values saved to 'daily_rsi.csv' file.")

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 185,
    "MSFT": 420
}

portfolio = {}
total = 0

print("=== Stock Portfolio Tracker ===")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found. Try again.")
        continue
    qty = int(input(f"Enter quantity for {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + qty

# Calculate and display
print("\n=== Your Portfolio ===")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total += value
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment: ${total}")

# Optional: Save to file
save = input("\nSave to file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio.csv", "w") as f:
        f.write("Stock,Quantity,Price,Value\n")
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            f.write(f"{stock},{qty},{stock_prices[stock]},{value}\n")
        f.write(f"Total,,,{total}\n")
    print("Saved to portfolio.csv!")
    
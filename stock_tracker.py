
import csv

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 350,
    "AMZN": 145
}

portfolio = []
total_investment = 0

print("=== Stock Portfolio Tracker ===")
print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
    print(stock, ":", price)

n = int(input("\nHow many stocks do you want to enter? "))

for i in range(n):
    stock = input("\nEnter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        price = stock_prices[stock]
        investment = price * quantity
        total_investment = total_investment + investment

        portfolio.append([stock, quantity, price, investment])

        print("Investment:", investment)
    else:
        print("Stock not available")

print("\n=== Portfolio Summary ===")

for item in portfolio:
    print(
        "Stock:", item[0],
        "Quantity:", item[1],
        "Price:", item[2],
        "Investment:", item[3]
    )

print("\nTotal Investment: $", total_investment)

with open("portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Stock", "Quantity", "Price", "Investment"])
    writer.writerows(portfolio)
    writer.writerow(["TOTAL", "", "", total_investment])

print("Portfolio saved to portfolio.csv")

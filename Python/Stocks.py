import random

stock_prices = []
days = int(input("Enter days in advance:"))

for i in range(0, days):
    stock_prices.append(random.randint(0, 1000))
    print(stock_prices[i], "on day", i)


def max_profit():
    low = 0
    high = 0
    maximum_profit = 0
    for x in range(0, days):
        for y in range(x, days):
            if stock_prices[y] - stock_prices[x] > maximum_profit:
                low = x
                high = y
                maximum_profit = stock_prices[y] - stock_prices[x]
    print("If you buy on day", low, "and sell on day", high, "then you will make", maximum_profit)

max_profit()


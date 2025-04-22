import random

def generate_stock_price():
    price = 100.0
    while True:
        daily_return = random.normalvariate(0, 0.01)  # Small % change
        price *= (1 + daily_return)
        yield round(price, 2)

# For testing
if __name__ == "__main__":
    stream = generate_stock_price()
    for _ in range(10):
        print(next(stream))
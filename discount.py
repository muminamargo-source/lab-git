def calculate_discount(price, discount_percent):
    return price * (100 - discount_percent) / 100

print(calculate_discount(1000, 20))
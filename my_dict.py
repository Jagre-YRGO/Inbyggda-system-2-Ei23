fuel_prices = {
    'today' : 21.84,
    'yesterday' : 22,
    'two_days_ago' : 21.7
}

accumulator = 0

for day, price in fuel_prices.items():
    print(f'Fuel price {day} is/was: {price}')
    accumulator += price

print(f'medelpris sista 3 dagarna: {accumulator/3}')

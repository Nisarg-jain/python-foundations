# 1. Base property pricing setup
house_price = 1_000_000
has_good_credit = True

# 2. Conditional branch to determine required down payment percentage
if has_good_credit:
    down_payment_rate = 0.10
else:
    down_payment_rate = 0.20

down_payment = house_price * down_payment_rate

print(f"Base Price: ${house_price:,}")
print(f"Down Payment Required: ${down_payment:,.2f}")

# 3. Multi-branch demonstration with temperature states
temperature = 22

if temperature > 30:
    weather_report = "Hot day: hydrate frequently."
elif temperature < 15:
    weather_report = "Cold day: wear warm clothing."
else:
    weather_report = "Moderate day: optimal conditions."

print(f"Status ({temperature}°C): {weather_report}")
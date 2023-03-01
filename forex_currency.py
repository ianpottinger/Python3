from forex_python.converter import CurrencyRates

# Create a CurrencyRates object
c = CurrencyRates()

# Get a list of all available currencies
currencies = c.get_rates('GBP')

# Loop through all currencies and print the exchange rate against GBP
for currency, rate in currencies.items():
    # Print the currency and the exchange rate against GBP
    print(f"{currency}: {rate}")

# Get a list of all available currencies
currencies = c.get_rates('USD')

# Loop through all currencies and print the exchange rate against USD
for currency, rate in currencies.items():
    # Print the currency and the exchange rate against USD
    print(f"{currency}: {rate}")

# Get a list of all available currencies
currencies = c.get_rates('EUR')

# Loop through all currencies and print the exchange rate against EUR
for currency, rate in currencies.items():
    # Print the currency and the exchange rate against EUR
    print(f"{currency}: {rate}")

# Get a list of all available currencies
currencies = c.get_rates('JPY')

# Loop through all currencies and print the exchange rate against JPY
for currency, rate in currencies.items():
    # Print the currency and the exchange rate against JPY
    print(f"{currency}: {rate}")

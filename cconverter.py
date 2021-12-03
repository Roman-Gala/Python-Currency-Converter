import json
import requests


# Definitions.
def add_to_cache(cache, main_currency, conv_currency):
    url = f'http://www.floatrates.com/daily/{main_currency}.json'
    rate = json.loads(requests.get(url).text)[conv_currency]['rate']
    cache[conv_currency] = rate


# User input main_currency.
while True:
    try:
        main_currency = input("Main currency: ").lower()
        if not main_currency:
            raise ValueError
    except ValueError:
        print("Try again.")
    else:
        break

# Cache
cache = {}
if main_currency != 'usd':
    add_to_cache(cache, main_currency, 'usd')
if main_currency != 'eur':
    add_to_cache(cache, main_currency, 'eur')

# Conversion
while True:
    conv_currency = input("Go-to currency: ").lower()
    if not conv_currency:
        break
    main_amount = float(input(f"Amount of {main_currency.upper()}: "))

    print("Checking the cache...")
    if conv_currency in cache.keys():
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        add_to_cache(cache, main_currency, conv_currency)
    received = cache[conv_currency] * main_amount
    print(f"Converted amount: {round(received, 2)} {conv_currency.upper()}.")

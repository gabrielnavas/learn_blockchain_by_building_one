import requests

url = 'https://api.coinbase.com/v2/prices/spot?currency=USD'
response = requests.get(url)
print(response.text)

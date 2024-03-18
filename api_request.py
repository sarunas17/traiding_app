import requests

url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=DHVVHGCAT5GZALII'
r = requests.get(url)
data = r.json()

print(data)

# A lightweight alternative to the time series APIs, 
# this service returns the latest price and volume information for a ticker of your choice.
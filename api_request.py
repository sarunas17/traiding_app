import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

def get_stock_price(stock_name: str) -> float:
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_name}&apikey={api_key}'    
    r = requests.get(url)
    data = r.json()
    print(data)    
    print(data["Global Quote"]['01. symbol'])
    print(data["Global Quote"]['05. price'])
    return data["Global Quote"]['05. price']

get_stock_price("IBM")
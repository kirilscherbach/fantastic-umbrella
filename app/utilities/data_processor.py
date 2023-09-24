import requests

def fetch_data(url):
    return requests.get(url).json()

def process_data(url):
    data = fetch_data(url)
    return sum(data) 


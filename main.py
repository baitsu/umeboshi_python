import requests

def main():
    url="http://example.com"
    response=requests.get(url)
    print(response)
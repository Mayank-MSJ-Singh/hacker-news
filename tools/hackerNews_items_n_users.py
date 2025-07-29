import requests

base_url = 'https://hacker-news.firebaseio.com/v0'



async def hackerNews_item(id):
    url = f"{base_url}/item/{id}.json"
    result = requests.get(url)
    return (result.json())

async def hackerNews_user(id):
    url = f"{base_url}/user/{id}.json"
    result = requests.get(url)
    return (result.json())

async def hackerNews_maxitem():
    url = f"{base_url}/maxitem.json"
    result = requests.get(url)
    return (result.json())
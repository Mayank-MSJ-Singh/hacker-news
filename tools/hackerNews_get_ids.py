import requests

base_url = 'https://hacker-news.firebaseio.com/v0'

async def hackerNews_topstories_ids():
    url = f"{base_url}/topstories.json"
    result = requests.get(url)
    return (result.json())

async def hackerNews_newstories_ids():
    url = f"{base_url}/newstories.json"
    result = requests.get(url)
    return (result.json())

async def hackerNews_askstories_ids():
    url = f"{base_url}/askstories.json"
    result = requests.get(url)
    return (result.json())

async def hackerNews_showstories_ids():
    url = f"{base_url}/showstories.json"
    result = requests.get(url)
    return (result.json())

async def hackerNews_jobstories_ids():
    url = f"{base_url}/jobstories.json"
    result = requests.get(url)
    return (result.json())

async def hackerNews_updates_ids():
    url = f"{base_url}/updates.json"
    result = requests.get(url)
    return (result.json())

async def hackerNews_beststories_ids():
    url = f"{base_url}/beststories.json"
    result = requests.get(url)
    return (result.json())

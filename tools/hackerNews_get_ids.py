import requests

base_url = 'https://hacker-news.firebaseio.com/v0'

def hackerNews_maxitem_ids():
    url = f"{base_url}/maxitem.json"
    result = requests.get(url)
    return (result.json())

def hackerNews_topstories_ids():
    url = f"{base_url}/topstories.json"
    result = requests.get(url)
    return (result.json())

def hackerNews_newstories_ids():
    url = f"{base_url}/newstories.json"
    result = requests.get(url)
    return (result.json())

def hackerNews_askstories_ids():
    url = f"{base_url}/askstories.json"
    result = requests.get(url)
    return (result.json())

def hackerNews_showstories_ids():
    url = f"{base_url}/showstories.json"
    result = requests.get(url)
    return (result.json())

def hackerNews_jobstories_ids():
    url = f"{base_url}/jobstories.json"
    result = requests.get(url)
    return (result.json())

def hackerNews_updates_ids():
    url = f"{base_url}/updates.json"
    result = requests.get(url)
    return (result.json())

def hackerNews_beststories_ids():
    url = f"{base_url}/beststories.json"
    result = requests.get(url)
    return (result.json())

if __name__ == '__main__':
    '''
    print("Top Stories: ",hackerNews_topstories_ids())
    print("New Stories: ",hackerNews_newstories_ids())
    print("Ask Stories: ",hackerNews_askstories_ids())
    print("Show Stories: ",hackerNews_showstories_ids())
    print("Job Stories: ",hackerNews_jobstories_ids())
    print("Best Stories: ",hackerNews_beststories_ids())
    '''
    print("Updates: ", hackerNews_updates_ids())
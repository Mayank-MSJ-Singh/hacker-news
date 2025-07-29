import asyncio
import json
from hackerNews_get_ids import (
    hackerNews_showstories_ids,
    hackerNews_beststories_ids,
    hackerNews_topstories_ids,
    hackerNews_newstories_ids,
    hackerNews_jobstories_ids,
    hackerNews_askstories_ids,
    hackerNews_updates_ids,
)
from hackerNews_items_n_users import hackerNews_item

base_url = 'https://hacker-news.firebaseio.com/v0'


async def hackerNews_topstories(count=5):
    ids = await hackerNews_topstories_ids()
    news = []

    for item_id in ids[:count]:
        item = await hackerNews_item(item_id)
        news.append(item)

    return json.dumps(news)


async def hackerNews_beststories(count=5):
    ids = await hackerNews_beststories_ids()
    news = []

    for item_id in ids[:count]:
        item = await hackerNews_item(item_id)
        news.append(item)

    return json.dumps(news)


async def hackerNews_newstories(count=5):
    ids = await hackerNews_newstories_ids()
    news = []

    for item_id in ids[:count]:
        item = await hackerNews_item(item_id)
        news.append(item)

    return json.dumps(news)


async def hackerNews_showstories(count=5):
    ids = await hackerNews_showstories_ids()
    news = []

    for item_id in ids[:count]:
        item = await hackerNews_item(item_id)
        news.append(item)

    return json.dumps(news)


async def hackerNews_askstories(count=5):
    ids = await hackerNews_askstories_ids()
    news = []

    for item_id in ids[:count]:
        item = await hackerNews_item(item_id)
        news.append(item)

    return json.dumps(news)


async def hackerNews_jobstories(count=5):
    ids = await hackerNews_jobstories_ids()
    news = []

    for item_id in ids[:count]:
        item = await hackerNews_item(item_id)
        news.append(item)

    return json.dumps(news)

async def hackerNews_updates(count=5):
    ids = await hackerNews_updates_ids()
    news = []
    profiles = ids['profiles'][:count]

    for item_id in ids['items'][:count]:
        item = await hackerNews_item(item_id)
        news.append(item)

    newlist = json.dumps({
        "items": news,
        "profiles": profiles
    })
    return newlist


from Eyes.lib.agents import user_agent
from Eyes.lib.requests import Requests
import random


async def duolingo(email):
    URL = "https://www.duolingo.com/2017-06-30/users"

    headers = {
        'user-agent': random.choice(user_agent())
    }

    params = {
        'email': email
    }

    try:
        r = await Requests(URL, params=params, headers=headers).get()

        if """{"users":[]}""" in r.text:
            return f"""No Duolingo account"""

        else:
            return f"""Duolingo account detected!
    ├──Name : {r.json()['users'][0]['username']}
    ├──Bio : {r.json()['users'][0]['bio']}
    ├──Total XP : {r.json()['users'][0]['totalXp']}
    └──From Language : {r.json()['users'][0]['courses'][0]['fromLanguage']}"""

    except Exception:
        return """🚧 Duolingo"""

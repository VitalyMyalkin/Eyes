from Eyes.lib.agents import user_agent
from Eyes.lib.requests import Requests

import random


async def gravatar(email):
    URL = "https://en.gravatar.com/{}.json"

    headers = {
        'user-agent': random.choice(user_agent())
    }

    try:
        r = await Requests(URL.format(email), headers).get()

        if "User not found" in r.text:
            return f"""No Gravatar account"""

        else:
            if r.json()['entry'][0]['displayName'] != None or '':
                return f""" Gravatar account detected!
    └──Name : {r.json()['entry'][0]['displayName']}
                    """

            else:
                return f"""Gravatar account detected, but no name displayed!"""

    except Exception:
        return """🚧 Gravatar"""

import random
from Eyes.lib.requests import Requests
from Eyes.lib.agents import user_agent



async def bitmoji(email):
    URL = "https://bitmoji.api.snapchat.com/api/user/find"

    headers = {
        'user-agent': random.choice(user_agent())
    }

    data = {
        'email': email
    }

    try:
        r = await Requests(URL, headers=headers, data=data).post()

        if '{"account_type":"snapchat"}' in r.text:
            return f"""Bitmoji account detected!"""

        else:
            return f"""No Bitmoji account"""

    except Exception:
        return """🚧 Bitmoji"""

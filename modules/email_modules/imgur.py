from Eyes.lib.agents import user_agent
from Eyes.lib.requests import Requests
import random


async def imgur(email):
    URL = "https://imgur.com/signin/ajax_email_available"

    headers = {
        'user-agent': random.choice(user_agent())
    }

    data = {
        'email': email
    }

    try:
        r = await Requests(URL, headers, data).post()

        if """{"data":{"available":false},"success":true,"status":200""" in r.text:
            return f"""Imgur account detected!"""

        else:
            return f"""No Imgur account"""

    except Exception:
        return """🚧 Imgur"""

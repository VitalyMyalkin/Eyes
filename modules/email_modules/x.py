from Eyes.lib.agents import user_agent
from Eyes.lib.requests import Requests
import random
import json


async def x(email):
    URL = "https://api.twitter.com/i/users/email_available.json?email={}"

    headers = {
        "user-agent": random.choice(user_agent())
    }

    try:
        r = await Requests(URL.format(email), headers).get()

        read = json.load(r)

        if read['taken'] == True:
            return f"""X (Twitter) account detected!"""

        else:
            return f"""No X (Twitter) account"""

    except Exception:
        return """🚧 X (Twitter)"""

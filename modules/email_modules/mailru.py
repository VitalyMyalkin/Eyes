from Eyes.lib.agents import user_agent
from Eyes.lib.requests import Requests

import random


async def mailru(email):
    URL = "https://account.mail.ru/api/v1/user/exists?email={}"

    headers = {
        'user-agent': random.choice(user_agent())
    }

    try:
        r = await Requests(URL.format(email), headers).get()

        try:
            if r.json()['body']['exists'] == True:
                return f"Mail.ru account detected"

            else:
                return f"No Mail.ru account"
        except:
            return f"No Mail.ru account"

    except Exception:
        return """🚧 Mail.ru"""

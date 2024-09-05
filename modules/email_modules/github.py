from Eyes.lib.agents import user_agent
from Eyes.lib.requests import Requests
import random

from Eyes.lib import venom
from Eyes.lib.image import get_hashed, fetch_img


async def github(email):
    URL = "https://api.github.com/search/users?q={}+in:email"

    headers = {
        'user-agent': random.choice(user_agent()),
        # optional but better results 'authorization': 'token YOUR_API_TOKEN'
    }

    try:
        r = await Requests(URL.format(email), headers).get()

        if '"total_count": 0' in r.text:
            return f"""No GitHub account"""

        else:
            try:
                items = r.json()['items']
                if not items:
                    pass

                name = items[0]['login']
                avatar = items[0]['avatar_url']

                default = "https://github.com/identicons/{}.png".format(name)

                img = await fetch_img(avatar)
                img_hashed = get_hashed(img)

                default_img = await fetch_img(default)
                deufault_hashed = get_hashed(default_img)

                if img_hashed == deufault_hashed:
                    return f"""GitHub account detected!
    - Name : {name}
    - Avatar : {avatar}
    - Default profile picture"""

                else:
                    await venom.Face.facial(url=avatar, name=name,
                                            output_path=f"facial_recognition/venom_output_{name}.jpg")

                    return f"""GitHub account detected!
    ─ Name : {name}
    ─ Avatar : {avatar}
    ─🤳 No default profile picture"""

            except Exception:
                return f"""No GitHub account"""
    except Exception:
        return "🚧 GitHub"

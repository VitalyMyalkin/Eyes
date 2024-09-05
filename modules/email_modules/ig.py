from Eyes.lib.agents import user_agent
from Eyes.lib.requests import Requests
import random


async def instagram(email):
    URL = "https://www.instagram.com/web/search/topsearch/?context=blended&query={}"

    headers = {
        'user-agent': random.choice(user_agent()),
    }

    try:
        r = await Requests(URL.format(email), headers).get()

        if r.status_code == 200:
            try:
                data = r.json()
                users = data.get('users', [])

                if not users:
                    return f"No Instagram account"
                else:
                    user_info = users[0].get('user', {})

                    username = user_info.get('username', '')
                    profile_pic_url = user_info.get('profile_pic_url', '')

                    if username and profile_pic_url:
                        return f"""Instagram account detected!
    - Username: {username}
    - Profile Picture: {profile_pic_url}"""
                    else:
                        return f"No Instagram account"

            except Exception:
                return f"No Instagram account"

    except Exception:
        return "🚧 Instagram"

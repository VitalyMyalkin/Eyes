from Eyes.lib.agents import user_agent
from Eyes.lib.requests import Requests
import random
import re
from datetime import datetime


async def protonmail(email):
    URL = "https://api.protonmail.ch/pks/lookup?op=index&search={}"

    headers = {
        'user-agent': random.choice(user_agent())
    }

    try:
        r = await Requests(URL.format(email), headers=headers).get()

        if "info:1:0" in r.text:
            return f"No ProtonMail account"

        elif "info:1:1" in r.text:
            pat1 = "2048:(.*)::"
            pat2 = "22::(.*)::"
            pat3 = "4096:(.*)::"

            regex_pat = [pat1, pat2, pat3]

            for regex in regex_pat:
                timestamp = re.search(regex, r.text)
                if timestamp:
                    dtimeobject = datetime.fromtimestamp(
                        int(timestamp.group(1)))
                    return f"""ProtonMail account detected!
    └──Date of creation : {dtimeobject} 🌐 (UTC)"""
                else:
                    continue

        else:
            return f"No ProtonMail account"

    except Exception:
        return "🚧 ProtonMail"

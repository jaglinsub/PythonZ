# import required modules
from types import SimpleNamespace

import json
import requests

url = "https://rest.apisandbox.zuora.com/oauth/token"
payload='client_id=210fe90a-8ef3-4339-a333-78d9239c2386&grant_type=client_credentials&client_secret=bYFhSiSTnLOhHmsxHcwnajfJ4VJj29viS%2B0itau7Z'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

def getToken123():
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    resJson = json.loads(response.text, object_hook=lambda d: SimpleNamespace(**d))

    print(resJson.access_token)
    # return json.dumps(resJson)
    return response.json()



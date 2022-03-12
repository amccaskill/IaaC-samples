import requests
import json
import pprint
# Get token and store in variable "token"
requests.packages.urlib3.disable_warnings()
url = "https://10.10.20.65/api/fdm/v5/fdm/token"

payload =  {"grant_type": "password", "username": "admin", "password":"Cisco1234"}
headers =  {"Accept": "application/json", "Content-type": "application/json"}

token_response = requests.post(
    url, headers=headers, data=json.dump(payload), verify=False
 )
token_response.raise_for_status()
if token_response.status_code == 200:
     print("Token Successfully Received...\n")

token = token_response.json()["access_token"]


get_url = "https://10.10.20.65/api/fdm/v5/object/networks"

get_headers = {"Accept": "application/json", "Content-type": "application/json"}

while get_url:
    response = requests.get(get_url, headers=headers, params={f"limit":2}, verify=False)
    response.raise_for_status()
    data = response.json()
    items = data["items"]
    print("\n")
    for item in items:
        name = item["name"]
        subtype = item["subType"]
        value =  item["value"]
        print(f"{name} is a {subtype} object with a value of {value}")

    try:
        get_url = data["paging"]['next'][0]
        if not get_url:
            break
    except IndexError:
        break
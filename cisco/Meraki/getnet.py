import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get('token')

base_url = 'https://api.meraki.com/api/v0'
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    'X-Cisco-meraki-API-Key': f"{api_key}"
}
org_url = "/organizations"

def get_net():
    try:
        org_response = requests.get(
            url=f"{base_url}{org_url}", headers=headers)
        if org_response.status_code == 200:
            orgs = json.loads(org_response.text)
            for org in orgs:
                if org['name'] == 'Purple Rain':
                    org_id = org['id']
                    print(org_id)
    except Exception as err:
        print(err)

    net_url = f"/{org_url}/{org_id}/networks"
    try:
        net_response = requests.get(url=f"{base_url}{net_url}", headers=headers)
        if net_response.status_code == 200:
            nets = json.loads(net_response.text)
            for net in nets:
                if net in nets['name'] == "Dolphin":
                    net_id = net['id']
    except Exception as err:
        print(err)
    return net_id



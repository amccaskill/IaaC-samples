from getnet import get_net
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get('token')

base_url = 'https://api.meraki.com/api/v0'
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    'X-Cisco-meraki-API-Key': f"{api_key}"
}

def get_ssid():
    net_id = get_net()
    ssids_url = f' /networks/{net_id}/ssids'
    try:
        ssids_response = requests.get(
            url=f"{base_url}{ssids_url}", headers=headers)
        print(ssids_response)
        if ssids_response.status_code == 200:
            ssids = json.loads(ssids_response.text)
            for ssid in ssids:
                if ssids['name'] == 'doctors office':
                    ssid_details = {}
                    ssid_details['id'] = ssid['number']
                    ssid_details['name'] = ssid['name']
                    ssid_details['status'] = ssid['enable']
                    return ssid_details
    except Exception as err:
        print(err)

ssid = get_ssid()
print(ssid)

        

from Meraki.getnet import get_net
from Meraki.getssid import get_ssid
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

def enable_ssid():
    net_id = get_net()
    ssid_info = get_ssid()
    ssid_number = ssid_info['id']
    if not ssid_info['status']:
        print('Status is False {ssid_info["status"]}')
        ssid_url = f'/networks/{net_id}/ssids/{ssid_number}'
        payload = {
            'name': ssid_info['name'],
            'enable': True
        }
        response =  requests.put(url=f"{base_url}{ssid_url}", headers=headers, data=json.dumps(payload))
        print(response.status_code)
        print(response)
        return response

if __name__ == "__main__":
    Flip = enable_ssid()
    print(Flip)
    




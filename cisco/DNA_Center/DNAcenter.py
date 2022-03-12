from lib2to3.pgen2 import token
from os import environ
import os
import sys
import json
import requests
import pprint
from requests.auth import HTTPBasicAuth
import time
import urllib3
urllib3.disable_warnings()
from dotenv import load_dotenv
load_dotenv()
username = os.environ.get("username")
password = os.environ.get("password")


class DnaCenterAPI:

    def __init__(self, host, username, password, verify=False):
        # self.host = host
        self.username = username
        self.password = password
        self.verify = verify
        self.headers = {"Content-Type": "application/json", "Accept": "application/json"}
        self.system_url = f"https://{host}/dna/system/api/v1"
        self.intent_url = f"https://{host}/dna/intent/api/v1"

       
    def loginnow(self):
        # user login with credentials, then API token is granted (X-Auth-Token)
        cred = (username, password)
        auth_response = requests.post(
            f'{self.system_url}/auth/token',
            auth = cred,
            headers={self.headers},
            verify=False
        )
        auth_response.raise_for_status()
        # return auth_response.json()["Token"]
        token = auth_response['Token']

    def getsites(self):
        dnac = DnaCenterAPI.loginnow(username, password)
        auth_token = token#dnac["Token"]
        auth_request = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "x-auth-token": token
        }
        sites = requests.get(url=f'{self.intent_url}/topology/site-topology')
        print(json.dumps(sites, indent=2))

    def getclienthealth(self):
        dnac = DnaCenterAPI.loginnow(username, password)
        auth_token = token#dnac["Token"]
        auth_request = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "x-auth-token": token
        }

        # Client Health Retrieval
       
        response = requests.get(
            f"{self.intent_url}/client-health", 
            headers=auth_request, verify=False)

        return response.json()['response']
        print(json.dumps(response, indent=3))
        print(f"{response['response'][0]['scoreDetail']}")
        scoreDetail = response['response'][0]['scoreDetail']
        
        poor_performance =  []
        good_performance = []

        for score in scoreDetail:
            if ['scoreValue'] <= 5:
                 poor_performance =+ 1
            else: 
                good_perfromance =+ 1

        print(f"there are {poor_performance} clients performing poorly")
        print(f"there are {good_performance} clients performing fine")
        









        if response




        







    def getdevices(self):
        dnac = DnaCenterAPI.loginnow(username, password)
        auth_token = token#dnac["Token"]
        auth_request = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "x-auth-token": token
        }
        device_node = f"{self.intent_url}/network-device"
        devices = requests.get(url=f'{self.system}/{device_node}',
        headers=auth_request,
        verify=False).json()['response']
        # print(json.dumps(devices, indent=2))
        for device in devices:
            if device['hostname'] == "Purple-core.gold.local":
                device_id = device['id']
        node_vlan = f"{self.intent_url}/network-device/{device_id}/vlan"
        node_vlans = requests.get(url=f"{self.intent_url}/{node_vlan}",
                                                headers=auth_request, verify=False).json()['response']
        print(json.dumps(node_vlans, indent=2))

    def devicediscovery(self):
        dnac = DnaCenterAPI.loginnow(username, password)
        auth_token = token#dnac["Token"]
        auth_request = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "x-auth-token": token
        }
        http_endpoint = '/intent/api/v1/global-credential?credentialSubType=HTTP_WRITE'
        http_cred = requests.get(
            url=f'{self.intent_url}/{http_endpoint}', headers=auth_request, verfiy=False).json()
        http_cred_id = http_cred['response'][0]['id']

        DISCOVERY_URL = '/dna/intent/api/v1/discovery'
        HTTP_WRITE_CREDENTIALS_URL = '/dna/intent/api/v1/global-credential/http-write'

        discovery = {
            "name": "Discovery-Guide",
            "discoveryType": "Range",
            "ipAddressList": "10.255.3.11-10.255.3.19",
            "protocolOrder": "http",
            "timeOut": 5,
            "retryCount": 3,
            "isAutoCdp": False,
            "globalCredentialIdList": [
                http_cred_id
            ]
            }
        response = requests.post(
            f"{self.intent_url} {DISCOVERY_URL}", headers=auth_request,
                 json=discovery, verify=False)

        print(json.dumps(response, indent=3))

        task_id = response.json()['response']['taskId']


        time.sleep(10)
        requests.get(
            f'{self.intent_url}/dna/intent/api/v1/task/{task_id}'.format(task_id), 
            headers=auth_request, verify=False)
        discovery_id = response['progress']






        
        





if __name__ == '__main__':
    DnaCenterAPI()
    










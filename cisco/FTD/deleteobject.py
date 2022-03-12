from lib2to3.pgen2 import token
import os
import json
import requests
import pprint

# Set up the delete request and the request for the token
requests.packages.urlib3.disable_warnings()
target = input("Enter the object you want to delete: ")
clear_screen = "clear"
os.system(clear_screen)

url = "https://10.10.20.65/api/fdm/v5/fdm/token"
auth_cred = {"grant_type": "password", "username": "admin", "password": "Cisco1234"}
headers = {"Accept": "application/json", "Content-Type": "application/json"}

token_response = requests.post(
    url, headers=headers, data=json.dumps(auth_cred), verify=False
)
token_response.raise_for_status()
if token_response.status_code == 200:
    print("Token received successfully")

# Take the token extracted from the last request and used to athenticate with it
token = token_response.json()["access_token"]
url =  "https://10.10.20.65/api/fdm/v5/object/networks"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer: {token}", 
}
# authenticate then loop thru items names. Once the items matches the user input, delete that object.
get_response = requests.get(url, headers=headers, verify=False).json()
items = get_response["items"]
name_list = []
for item in items:
    addname = item["name"]
    name_list.append(addname)
    if item["name"] == target:
        targetname = item["name"]
        objectId = item["id"]
        url = f"https://10.10.20.65/api/fdm/v5/object/networks/{objectId}"
        del_response = requests.delete(url, headers=headers, verify=False)
        del_response.raise_for_status()
        if del_response.status_code == 204:
            print(f"Deleted: {targetname} Object")

if target not in name_list:
    print(f"the object {targetname} does not exist currently")




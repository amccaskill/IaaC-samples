import requests

requests.packages.urlib3.disable_warnings()
router = {
    "host": "192.168.31.101",
    "port": "443",
    "user": "john",
    "password": "cisco123"
}

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

# to retrieve the model
url = f"https://{router['host']}:{router['port']}/restconf/data/native"

# The starting URI for all interface configuration data is https://host/restconf/data/Cisco‐IOS‐XEnative: native/interface/
# https://host/restconf/data/Cisco‐IOS‐XE‐native:native/interface/Vlan=10/
# https://host/restconf/data/Cisco‐IOS‐XE‐native:native/ip/route/


# use the model to retrieve specific config information
url = f"https://{router['host']}:{router['port']}/restconf/data/native/interface"
with open(add_loopback.yml, 'r') as loopback:
    config_int = yaml.safe_load(loopback)



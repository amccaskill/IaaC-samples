from scrapli_netconf.driver import NetconfScrape

device = {
    "host": "10.10.1.2",
    "auth_username": "cisco",
    "auth_password": "cisco",
    "auth_strict_key": False,
    "port": 830
}

conn = NetconfScrape(**device)
conn.open()

bgp_filter = """
<Cisco-IOS-XE-bgp>
    <bgp -id> 1454 </bgp -id>
</Cisco-IOS-XE-bgp>
"""

response = conn.get(
    filter_=bgp_filter, filter_type='subtree')
print(response.result)


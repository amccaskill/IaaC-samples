from cgitb import text
import requests
import xmltodict
import pprint as print
import os
from dotenv import load_dotenv

load_dotenv()
username = os.environ.get('username')
password = os.environ.get('password')
host = os.environ.get('host')

class UcsTemplate:
    def __init__(self,  username, password, host):
        self.host = host
        self.username = username
        self.password = password
        self.cookie = None

    def ucs_request(self):
        response1 = requests.post(
            f"http://{self.host}/nuova",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=f'<aaaLogin inName="{self.name}" inPassword="{self.pasword}"/>',
        )
        response1.raise_for_status()

        status = response1.status_code
        if status[0] == 200:
            resp_data = xmltodict.parse(response1.text)
            pull_cookie = resp_data["aaaLogin"]["@outCookie"]
            # return(status, resp_data)

        build_temp = f"""
        <lsInstantiateNTemplate
            dn="org-root/ls-testtemplate"
            cookie="{pull_cookie}"
            inTargetOrg="org-root"
            inServerNamePrefixOrEmpty="BigServer"
            inNumberOf="7"
            inHierarchical="no">
        </lsInstantiateNTemplate>
        """

    #  build_server_template
        request2 = requests.post(
        f"http://{self.host}/nuova",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=f"{build_temp}",
        )
        status2 = request2.raise_for_status()
        if status2[0] == 200:
            results = xmltodict.parse(request2.text)
            titles = results['lsInstantiateNTemplate']['outConfig']['lsServer']
            for server in titles:
                template = server['@srcTemplName']
                name = server['@name']
                id = server['@intId']
                print(f'Server {name} Server_ID {id} from {template}')
            
if __name__ == "__main__":
    UcsTemplate()
import requests
from requests.structures import CaseInsensitiveDict

def check_url(url_path):
    # url = "https://raw.githubusercontent.com/organization/repo/branch/folder/file"
    #url = "https://raw.githubusercontent.com/phonkriminal/Hackintosh-Dell-G7-Monterey/main/README.md"
    # If repo is private - we need to add a token in header:
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "token TOKEN"

    resp = requests.get(url_path)#, headers=headers)
    return resp.status_code


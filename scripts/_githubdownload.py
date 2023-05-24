import urllib.request
from _download import check_url

def get_appfiles(url):
    
    urllib.request.urlretrieve(url, 'Hackintools.tar')

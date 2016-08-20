import requests

def server_check(url):
    try:
        resp = requests.get(url)
        if resp.ok:
            url_status = 1
        else:
            url_status = 0
    except requests.exceptions.RequestException as e:
        url_status = 0
    return url_status
import os
import requests
from .. import log

def post_data(url, data=None, json=None, proxies=None, system_proxy=False, verify=True):
    headers = {
        "User-Agent": "adogecheems/aninfo/1.0.0 (https://github.com/adogecheems/an-info)"
    }

    if system_proxy:
        http_proxy = os.environ.get('http_proxy')
        https_proxy = os.environ.get('https_proxy')
        if http_proxy or https_proxy:
            proxies = {'http': http_proxy, 'https': https_proxy}
        else:
            log.warning("No system proxy found.")
            raise requests.exceptions.ProxyError("No system proxy found.")

    try:
        if not verify:
            requests.packages.urllib3.disable_warnings()

        response = requests.post(url, data=data, json=json, headers=headers, proxies=proxies, verify=verify)
        log.debug(f"A request has been made to url: {url}")
        return response

    except requests.RequestException as e:
        log.exception(f"The search was aborted due to network reasons: {e}")
        raise

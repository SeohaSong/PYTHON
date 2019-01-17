
import re
import requests


def get_public_ip():        
    parser = re.compile(r"\d{2,3}\.\d{2,3}\.\d{2,3}\.\d{2,3}")
    urls = [
        "http://ip.42.pl/raw",
        "https://jsonip.com/",
        "http://httpbin.org/ip",
        "https://api.ipify.org/",
        "https://ipecho.net/plain"    
    ]
    for url in urls:
        res = requests.get(url)
        if not res.status_code == 200:
            continue
        result = parser.search(str(res.content))
        if not result:
            continue
        ip = result.group(0)
        break
    return ip

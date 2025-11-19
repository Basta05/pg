import sys
import requests
import re

def download_url_and_get_all_hrefs(url):
    hrefs = []

    response = requests.get(url)

    if response.status_code == 200:
        hrefs = re.findall(r'<a[^>]*href="([^"]+)"', response.text)

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        data = download_url_and_get_all_hrefs(url)
        print(data)
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
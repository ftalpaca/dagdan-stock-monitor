import requests
from bs4 import BeautifulSoup
import time
import config


def fetch_page(url: str):
    headers = {"User-Agent": config.USER_AGENT}

    for attempt in range(config.MAX_RETRIES):
        try:
            r = requests.get(url, headers=headers, timeout=config.REQUEST_TIMEOUT)
            if r.status_code == 200:
                return r.text
        except requests.RequestException:
            time.sleep(2 ** attempt)

    return None


def normalize(text):
    return " ".join(text.lower().split())


def detect_stock(html, retailer):
    soup = BeautifulSoup(html, "html.parser")
    text = normalize(soup.get_text(" "))

    positive = sum(p in text for p in retailer["positive"])
    negative = sum(n in text for n in retailer["negative"])

    if negative >= 2:
        return False

    if positive > 0 and negative == 0:
        return True

    return False


def check_all():
    results = {}

    for name, data in config.RETAILERS.items():
        html = fetch_page(data["url"])
        if not html:
            results[name] = False
            continue

        results[name] = detect_stock(html, data)

    return results

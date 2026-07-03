import requests
import datetime


def notify(webhook, retailer, url):
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    payload = {
        "content": (
            f"🚨 **{retailer} IN STOCK**\n\n"
            f"{url}\n\n"
            f"{now}"
        )
    }

    requests.post(webhook, json=payload, timeout=10)

PRODUCT_NAME = "Fire Emblem: Fortune's Weave – Dagdan Collection"

CHECK_INTERVAL_MINUTES = 15

REQUEST_TIMEOUT = 20

MAX_RETRIES = 3

USER_AGENT = (
    "Mozilla/5.0 "
    "(Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 "
    "(KHTML, like Gecko) "
    "Chrome/137.0 Safari/537.36"
)

RETAILERS = {
    "Nintendo Store Ireland": {
        "url": "https://store.nintendo.com/en-ie/fire-emblem-fortunes-weave-dagdan-collection-P00199",
        "positive": ["add to cart", "buy now", "pre-order", "add to basket"],
        "negative": ["out of stock", "currently unavailable", "sold out"]
    },
    "Smyths Toys Ireland": {
        "url": "https://www.smythstoys.com/ie/en-ie/gaming-and-tech/pre-order-games/nintendo-switch-2-pre-order-games/fire-emblem-fortunes-weave-dagdan-collection-nintendo-switch-2/p/263444",
        "positive": ["add to basket", "pre-order", "buy now"],
        "negative": ["out of stock", "sold out", "notify me"]
    }
}

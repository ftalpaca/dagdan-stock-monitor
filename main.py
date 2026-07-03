import config
from checker import check_all
from state import load_state, save_state
from notifier import notify


DISCORD_WEBHOOK = https://discord.com/api/webhooks/1522403734993502229/zmtCvR0yzs1mYTkD4d_1BVNFjbp01V_29jnxtOLG5PIIFqZpQaEweznWwZPbzpQP845Q


def run():
    previous = load_state()
    current = check_all()

    for retailer, in_stock in current.items():
        was_in_stock = previous.get(retailer, False)

        # notify ONLY on change (false -> true)
        if in_stock and not was_in_stock:
            notify(
                DISCORD_WEBHOOK,
                retailer,
                config.RETAILERS[retailer]["url"]
            )

    save_state(current)


if __name__ == "__main__":
    run()

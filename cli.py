import argparse
from bot.client import BinanceClient
from bot.orders import place_order
from bot.logging_config import setup_logger

logger = setup_logger()

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    print("\n=== ORDER REQUEST ===")
    print(vars(args))

    client = BinanceClient().get_client()

    try:
        response = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n=== ORDER SUCCESS ===")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice')}")

    except Exception as e:
        print("\n=== ORDER FAILED ===")
        print(str(e))


if __name__ == "__main__":
    main()
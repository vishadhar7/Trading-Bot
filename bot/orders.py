from bot.validators import *
import logging

logger = logging.getLogger("trading_bot")

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        # Validate inputs
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(price, order_type)

        logger.info(f"Placing order: {symbol} {side} {order_type} {quantity} {price}")

        if order_type == "MARKET":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
        else:
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logger.info(f"Response: {response}")

        return response

    except Exception as e:
        logger.error(f"Error placing order: {str(e)}")
        raise
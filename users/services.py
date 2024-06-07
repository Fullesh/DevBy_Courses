import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(instance):
    product_title = f'{instance.course}' if instance.course else f'{instance.lession}'
    stripe_product = stripe.Product.create(name=f"{product_title}")
    return stripe_product.get('id')


def create_stripe_price(stripe_product_id, amount):
    return stripe.Price.create(
        currency='rub',
        unit_amount=int(amount * 100),
        product=stripe_product_id,)


def create_stripe_session(price):
    session = stripe.checkout.Session.create(success_url="http://127.0.0.1:8000/users/payments/list",
                                             line_items=[{"price": price.get("id"), "quantity": 1}],
                                             mode="payment")
    return session.get("id"), session.get("url")
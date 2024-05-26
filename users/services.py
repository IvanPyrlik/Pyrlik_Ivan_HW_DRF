import stripe
from forex_python.converter import CurrencyRates
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def convert_rub_to_dollars(amount):
    """
    Конвертер - рубли в доллары.
    """
    c = CurrencyRates()
    rate = c.get_rate('RUB', 'USD')
    return int(amount * rate)


def create_stripe_product(product_name):
    """
    Создаем продукт в страйпе.
    """
    product = stripe.Product.create(name=product_name)
    return product['id']


def create_stripe_price(amount, product_id):
    """
    Создаем цену в страйпе.
    """
    price = stripe.Price.create(unit_amount=amount * 100, currency='rub', product=product_id)
    return price['id']


def create_stripe_sessions(price):
    """
    Создаем сессию на оплату в страйпе.
    """
    session = stripe.checkout.Session.create(
        success_url='http://127.0.0.1:8000/user/payments/',
        line_items=[{'price': price.get('id'), 'quantity': 1}],
        mode='payment',
    )

    return session.get('url'), session.get('id')

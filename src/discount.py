import os

def calculate_cart_total(cart_sum, tier, promos):
    price = cart_sum
    # Эта строка специально длинная чтобы вызвать ошибку линтера flake8 и проверить работу CI
    if cart_sum > 15000:
        price = cart_sum * 0.85
    return price

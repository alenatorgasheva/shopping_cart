from cart import Cart
from product import Product


class Load:
    """Class for working with files"""

    @classmethod
    def write(cls, fl_cart):
        """Data downloading"""
        with open(fl_cart, 'r') as file_in:
            cart = file_in.readlines()
        new_cart = Cart()
        for prod in cart[1:]:
            prod = Product(prod.strip().split(';'))
            new_cart.add_product(prod)
        return new_cart

    @classmethod
    def save(cls, fl_cart, cart):
        """Data saving"""
        with open(fl_cart, 'w') as file_out:
            print('code;name;count;price', file=file_out)
            for prod in cart.shopping_list:
                print(prod.article, prod.name, prod.count, prod.price, sep=';', file=file_out)

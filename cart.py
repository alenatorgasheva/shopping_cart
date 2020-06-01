class Cart:
    """Class of shopping carts"""

    def __init__(self):
        """Initialization"""
        self.shopping_list = []
        self.cost = 0

    def __str__(self):
        """String performance"""
        if not self.shopping_list:
            s = 'Корзина пуста.'
        else:
            s = '+' + '-' * 122 + '+\n'
            s += '|{:^60}|{:^16}|{:^12}'.format('Наименование', 'Производитель', 'Количество')
            s += '|{:^15}|{:^15}|'.format('Цена, р.', 'Стоимость, р.') + '\n'
            s += '|' + '-' * 122 + '|\n'
            for prod in self.shopping_list:
                s += prod.__str__() + '\n'
            s += '|' + '-' * 122 + '|\n'
            s += '|{:>89} | {:<30}|'.format('Общая стоимость', self.cost) + '\n'
            s += '+' + '-' * 122 + '+'
        return s

    def add_product(self, product):
        """Product addition"""
        self.shopping_list.append(product)
        self.cost += product.price * product.count

    def del_product(self, product_article):
        """Product removal"""
        for prod in self.shopping_list:
            if prod.article == product_article:
                self.shopping_list.remove(prod)
                self.cost -= prod.count * prod.price
                return False
        return True

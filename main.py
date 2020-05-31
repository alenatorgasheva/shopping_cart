# Project - study
# Shopping cart

# Developed by A.Torgasheva

from decode import code


class Load:

    @classmethod
    def write(cls, fl_cart):
        """Загрузка данных"""
        with open(fl_cart, 'r') as file_in:
            cart = file_in.readlines()
        new_cart = Cart()
        for prod in cart[1:]:
            prod = Product(prod.strip().split(';'))
            new_cart.add_product(prod)
        return new_cart

    @classmethod
    def save(cls, fl_cart):
        """ """
        with open(fl_cart, 'w') as file_out:
            print('code;name;count;price', file=file_out)
            for prod in Cart.shopping_list:
                print(prod.article, prod.name, prod.count, prod.price, sep=';', file=file_out)


class Cart:
    """ """

    def __init__(self):
        self.shopping_list = []
        self.cost = 0

    def __str__(self):
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
            s += '+' + '-' * 122 + '+\n'
        return s

    def add_product(self, product):
        """ """
        self.shopping_list.append(product)
        self.cost += product.price * product.count

    def del_product(self, product_article):
        """ """
        pass


class Product:
    """ """
    price = property()
    article = property()

    def __init__(self, prod):
        self.__article = prod[0]
        if prod[0][:2] in code:
            self.__country = code[prod[0][:2]]
            self.__mfg_code = prod[0][2:7]
        else:
            self.__country = code[prod[0][:3]]
            self.__mfg_code = prod[0][3:7]
        self.__product_code = prod[0][7:12]
        self.__check_digit = prod[0][12]

        self.name = prod[1]
        self.count = int(prod[2])
        self.__price = float(prod[3])

    def __str__(self):
        s = '| {:<59}|{:^16}'.format(self.name, self.__country)
        s += '|{:^12}|{:^15.02f}|{:^15.02f}|'.format(self.count, self.price, self.count * self.price)
        return s

    def __repr__(self):
        return self.__str__()

    @price.setter
    def price(self, new_price):
        self.__price = new_price

    @price.getter
    def price(self):
        return self.__price

    @article.getter
    def article(self):
        s = 'Страна-производитель: {}\n'.format(self.__country)
        s += 'Код производителя:    {}\n'.format(self.__mfg_code)
        s += 'Контрольная цифра:    {}'.format(self.__check_digit)
        return s

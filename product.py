from decode import code


class Product:
    """Class of products"""
    price = property()
    article = property()

    def __init__(self, prod):
        """Initialization"""
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
        """String performance"""
        s = '| {:<59}|{:^16}'.format(self.name, self.__country)
        s += '|{:^12}|{:^15.02f}|{:^15.02f}|'.format(self.count, self.price, self.count * self.price)
        return s

    def __repr__(self):
        """Performance"""
        return self.__str__()

    @price.setter
    def price(self, new_price):
        """Setting price"""
        self.__price = new_price

    @price.getter
    def price(self):
        """Getting price"""
        return self.__price

    @article.getter
    def article(self):
        """Getting product article"""
        return self.__article

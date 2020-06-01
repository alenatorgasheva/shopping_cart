# Project - study
# Shopping cart

# Developed by A.Torgasheva

from load import Load
from cart import Cart
from product import Product

MENU = 'Выберите действие из списка:\n' \
       '\t1 - загрузить данные о корзине\n' \
       '\t2 - посмотреть данные о корзине\n' \
       '\t3 - добавить товар в корзину\n' \
       '\t4 - удалить товар из корзины'

POST_MENU = '\t1 - продолжить работу\n' \
            '\t2 - сохранить и продолжить\n' \
            '\t3 - сохранить и выйти\n' \
            '\t4 - выйти без сохранения'

cart = Cart()
while True:
    while True:
        print(MENU)
        choice = input()
        print('-' * 100)
        if choice == '1':
            fl_cart = input('Введите название файла: ')
            cart = Load.write(fl_cart)
            print('Данные загружены.')
            break

        elif choice == '2':
            print(cart)
            break

        elif choice == '3':
            prod_info = []
            print('Штрих-код продукта:', end=' ')
            s = input()
            prod_info.append(s)
            print('Наименование:', end=' ')
            s = input()
            prod_info.append(s)
            print('Количество:', end=' ')
            s = input()
            prod_info.append(s)
            print('Цена:', end=' ')
            s = input()
            prod_info.append(s)
            cart.add_product(Product(prod_info))
            print('Товар добавлен в корзину.')
            break

        elif choice == '4':
            print('Штрих-код продукта:', end=' ')
            s = input()
            if cart.del_product(s):
                print('Товар не найден.')
            else:
                print('Товар удален.')
            break
        print('Выбор некорректен.')
    print('-' * 100)

    print(POST_MENU)
    choice = input()
    print('-' * 100)

    if choice == '1':
        continue

    elif choice == '2':
        fl_cart = input('Введите название файла: ')
        Load.save(fl_cart, cart)
        continue

    elif choice == '3':
        fl_cart = input('Введите название файла: ')
        Load.save(fl_cart, cart)
        break

    elif choice == '4':
        print('Вы уверены, что хотите выйти без сохранения? (да, нет)')
        choice = input()
        if choice == 'да':
            break
        elif choice == 'нет':
            fl_cart = input('Введите название файла: ')
            Load.save(fl_cart, cart)
            break

print('Работа завершена.')

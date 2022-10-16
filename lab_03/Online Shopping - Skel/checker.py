#!/usr/bin/python3

import product as prod
import phone as ph
import refrigerator as rf
import stock as stk
import cart
import store
from io import StringIO
import sys
import os

def test_task(number):
    
    with open("tests/out/test_1.out") as f:
        output = f.readlines()

    with open("tests/ref/test_1.ref") as f:
        ref = f.readlines()

    if output == ref:
        print(f"TEST {number} .................. PASSED")
    else:
        print(f"TEST {number} .................. FAILED")

if __name__ == '__main__':

    print('****************  ONLINE SHOPPING - STARTED  *********************')
    # See if out dir exists
    path = os.getcwd() + "/tests/out"
    try:
        os.mkdir(path)
    except OSError:
        print(end = "")

    # Setting original stdout
    original_stdout = sys.stdout

    output = ""
    ref = ""

    test_product = prod.Product('Samsung Toaster', 20)
    test_phone = ph.Phone('Iphone 5', 60, '2GB', 'Apple A6')
    test_refrigerator = rf.Refrigerator('Gorenje Light 230', 150, 'A+')

    # # Test print message in Phone and Refrigerator
    sys.stdout = open("tests/out/test_1.out", 'w')
    print(test_phone)
    print(test_refrigerator)
    sys.stdout = original_stdout
    test_task(1)

    #print('*************************************')

    # # Test addition in Product
    sys.stdout = open("tests/out/test_2.out", 'w')
    print(test_phone + test_refrigerator)
    sys.stdout = original_stdout
    test_task(2)
    #print('*************************************')

    # Test Stock
    list_products = []
    list_products.append(ph.Phone('Iphone 12', 300, '4GB', 'A14 Bionic'))
    list_products.append(ph.Phone('Samsung Galaxy S20', 200, '8GB', 'Exynos Octa-core'))
    list_products.append(ph.Phone('Huawei P40', 250, '6GB', 'Exynos Octa-core'))
    list_products.append(rf.Refrigerator('Arctic CR-420', 500, 'A+'))
    list_products.append(rf.Refrigerator('Heinner CR-20', 100, 'A'))
    stock = stk.Stock(list_products)

    # Test view method in Stock
    sys.stdout = open("tests/out/test_3.out", 'w')
    for product in stock.view():
        print(product)
    sys.stdout = original_stdout
    test_task(3)
    #print('*************************************')

    # Test add and remove methods in Stock
    stock.add(ph.Phone('Iphone 5', 160, '2GB', 'Apple A8'))
    stock.remove('Huawei P40')

    sys.stdout = open("tests/out/test_4.out", 'w')
    for product in stock.view():
        print(product)
    sys.stdout = original_stdout
    test_task(4)
    #print('*************************************')

    # Test Cart
    cart = cart.Cart()

    # Test add, remove and view in Cart
    cart.add(ph.Phone('Iphone 5', 100, '2GB', 'Apple A8'))
    cart.add(ph.Phone('Iphone 12', 200, '8GB', 'Apple A16'))
    cart.add(rf.Refrigerator('Arctic E-100', 800, 'A+'))
    cart.remove('Iphone 5')

    sys.stdout = open("tests/out/test_5.out", 'w')
    for product in cart.view():
        print(product)
    sys.stdout = original_stdout
    test_task(5)
    #print('*************************************')

    # Test checkout method in Cart
    sys.stdout = open("tests/out/test_6.out", 'w')
    print(cart.cart_checkout())
    sys.stdout = original_stdout
    test_task(6)
    #print('*************************************')

    # # Test Store
    stock = stk.Stock(list_products)
    store = store.Store(stock)

    # Test login in Store
    store.login('batgirl123')
    store.login('pavelintruder1')

    sys.stdout = open("tests/out/test_7.out", 'w')
    print('batgirl123' in store.customer_carts)
    print('raduintruder' in store.customer_carts)
    sys.stdout = original_stdout
    test_task(7)
    #print('*************************************')

    # Test add_to_cart in Store
    store.add_to_cart('batgirl123', 'Iphone 12')
    store.add_to_cart('pavelintruder1', 'Megaphone X')

    sys.stdout = open("tests/out/test_8.out", 'w')
    for product in store.view_cart('pavelintruder1'):
        print(product)
    print()
    for product in store.stock.view():
        print(product)
    sys.stdout = original_stdout
    test_task(8)
    #print('*************************************')

    # Test remove_from_cart in Store
    store.remove_from_cart('batgirl123', 'Iphone 12')

    sys.stdout = open("tests/out/test_9.out", 'w')
    for product in store.customer_carts['batgirl123'].view():
        print(product)
    print()
    for product in store.stock.view():
        print(product)
    sys.stdout = original_stdout
    test_task(9)
    #print('*************************************')

    # Test view_cart and checkout in Store
    store.add_to_cart('batgirl123', 'Samsung Galaxy S20')
    store.add_to_cart('batgirl123', 'Heinner CR-20')

    sys.stdout = open("tests/out/test_10.out", 'w')
    for pair in store.view_cart('batgirl123'):
        print(pair)
    print(store.checkout('batgirl123'))

    sys.stdout = original_stdout
    test_task(10)

    print('****************  ONLINE SHOPPING - COMPLETED  *********************')
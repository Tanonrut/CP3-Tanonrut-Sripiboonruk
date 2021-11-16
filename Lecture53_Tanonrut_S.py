def vatCalaculate(price):
    resalt = price + (price * 7 / 100)
    return resalt


itemPrice = int(input("Please input your item price >>>"))
print(vatCalaculate(itemPrice))
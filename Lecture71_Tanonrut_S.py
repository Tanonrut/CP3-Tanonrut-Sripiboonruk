def showBill():
    totalPrice = 0
    print("------My Food-----")
    for i in range(len(menuList)):
        print(menuList[i], priceList[i])
        totalPrice += int(priceList[i])
    print("Total price : ", totalPrice)

menuList = []
priceList =[]
while True:
    menuName = input("Please enter menu >>> ")
    if menuName.lower() == 'exit':
        break
    else:
        menuPrice = input("Please input menu price >>> ")
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
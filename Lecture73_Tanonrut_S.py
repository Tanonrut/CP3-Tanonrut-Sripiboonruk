def showBill1():
    print("------My Food-----")
    for i in range(len(menuList)):
        print(menuList[i][0], menuList[i][1])

menuAdd = {}
menuList = []
while True:
    menuName = input("Please enter menu >>> ")
    if menuName.lower() == 'exit':
        break
    else:
        menuPrice = int(input("Please input menu price >>> "))
        menuAdd[menuName] = menuPrice
        menuList.append([menuName, menuAdd[menuName]])
showBill1()
userSelected = input("Please choose your menu >>> ")
print(menuAdd[userSelected])
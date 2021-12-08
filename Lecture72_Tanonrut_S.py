def showBill1():
    print("------My Food-----")
    for i in range(len(menuList)):
        print(menuList[i][0])
    for y in range(len(menuList)):
        print(menuList[y][1])

def showBill2():
    for number in range(len(menuList)):
        print(menuList[number][0])
        print(menuList[number][1])

menuList = []
while True:
    menuName = input("Please enter menu >>> ")
    if menuName.lower() == 'exit':
        break
    else:
        menuPrice = input("Please input menu price >>> ")
        menuList.append([menuName, menuPrice])
showBill1()
showBill2()
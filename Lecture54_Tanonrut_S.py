def register():
    print("!!! Register account !!!")
    registerName = input("Create username : ")
    registerPassword = int(input("Create password : "))
    return signIn(registerName, registerPassword)
def signIn(userName, passWord):
    print("!! Please Sign In !!")
    usernameInput = input("Input your username : ")
    passwordInput = int(input("Input your password : "))
    while userName != usernameInput or passWord != passwordInput:
        print("! Please sign in again !")
        usernameInput = input("Input your username : ")
        passwordInput = int(input("Input your password : "))
    print("Welcome Back to Ben Coffe & Food !!")
def showMenu():
    print("---------------------------------")
    print("!! Menu of Ben Coffe & Food !!")
    print("---------------------------------")
    print("NO. Menu            Price")
    print("---------------------------------")
    print("1. Coffee          60 THB")
    print("2. Fried rice     120 THB")
    print("3. Noodle          80 THB")
    print("4. Fried chicken  120 THB")
    print("5. Ice cream       40 THB")
    print("---------------------------------")
def menuPrice():
    coffeeSelected = 60
    friedRiceSelected = 120
    noodleSelected = 80
    friedChickenSelected = 120
    iceCreamSelected = 40
    return menuSelected(coffeeSelected, friedChickenSelected, noodleSelected,friedRiceSelected, iceCreamSelected)
def menuSelected(coffee, friedRice, noodle, friedChicken, iceCream):
    resultPrice = 0
    userSelectProcess = 1
    while userSelectProcess == 1:
        showMenu()
        print("Please choose number of a item which you want and amount")
        userSelectItem = int(input("Item number : "))
        userSelectAmount = int(input("Amount : "))
        if userSelectItem == 1:
            itemPrice = coffee * userSelectAmount
            print("Coffee ", userSelectAmount, "X", coffee,
                " = ", itemPrice, "THB")
            resultPrice = resultPrice + int(itemPrice)
        elif userSelectItem == 2:
            itemPrice = friedRice * userSelectAmount
            print("Fried rice ", userSelectAmount, "X", friedRice,
                " = ", itemPrice, "THB")
            resultPrice = resultPrice + int(itemPrice)
        elif userSelectItem == 3:
            itemPrice = noodle * userSelectAmount
            print("Noodle ", userSelectAmount, "X", noodle,
                " = ", itemPrice, "THB")
            resultPrice = resultPrice + int(itemPrice)
        elif userSelectItem == 4:
            itemPrice = friedChicken * userSelectAmount
            print("Fired Chicken ", userSelectAmount, "X", friedChicken,
                " = ", itemPrice, "THB")
            resultPrice = resultPrice + int(itemPrice)
        elif userSelectItem == 5:
            itemPrice = iceCream * userSelectAmount
            print("Ice Cream ", userSelectAmount, "X", iceCream,
                " = ", itemPrice, "THB")
            resultPrice = resultPrice + int(itemPrice)
        else:
            print("Something wrong !!!. Please try again")
            resultPrice = resultPrice
        print("DO you want something more? (Yes = 1 / No = 0)")
        userSelectProcess = int(input(">>>  "))
        while userSelectProcess >= 2:
            print("Something wrong !!!. Please try again")
            print("DO you want something more? (Yes = 1 / No = 0)")
            userSelectProcess = int(input(">>>  "))
    return piceCalculate(resultPrice)
def piceCalculate(totalPrice):
    print("---------------------------------")
    print("Total        =    ", float(totalPrice), " THB")
    print("Vat          =       7  %")
    print("Total price  =    ", totalPrice * float(1.07), " THB")
    print("---------------------------------")

register()
menuPrice()
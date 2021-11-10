print("!!! Register account !!!")
username = input("Create username : ")
password = int(input("Create password : "))
print ("!! Sign In !!")
usernameInput = input("Input your username : ")
passwordInput = int(input("Input your password : "))
if username == usernameInput and password == passwordInput:
    print("Welcome Back to Ben Coffe & Food !!")
    print("---------------------------------")
    print("NO. Menu            Price")
    print("---------------------------------")
    print("1. Coffee          60 THB")
    coffee = 60
    print("2. Fried rice     120 THB")
    friedRice = 120
    print("3. Noodle          80 THB")
    noodle = 80
    print("4. Fried chicken  120 THB")
    friedChicken = 120
    print("5. Ice cream       40 THB")
    iceCream = 40
    print("---------------------------------")
    print("Please choose number of a item which you want and amount")
    userSelectItemOne = int(input("Item number : "))
    userSelectAmountOne = int(input("Amount : "))
    if userSelectItemOne == 1 :
        priceOne = coffee * userSelectAmountOne
        print("Coffee ",userSelectAmountOne,"X",coffee,
              " = ",priceOne,"THB")
        itemOne = int(priceOne)
    elif userSelectItemOne == 2:
        priceOne = friedRice * userSelectAmountOne
        print("Fried rice ",userSelectAmountOne,"X",friedRice,
              " = ",priceOne,"THB")
        itemOne = int(priceOne)
    elif userSelectItemOne == 3:
        priceOne = noodle * userSelectAmountOne
        print("Noodle ", userSelectAmountOne, "X", noodle,
              " = ", priceOne, "THB")
        itemOne = int(priceOne)
    elif userSelectItemOne == 4:
        priceOne = friedChicken * userSelectAmountOne
        print("Fired Chicken ",userSelectAmountOne,"X",friedChicken,
              " = ",priceOne,"THB")
        itemOne = int(priceOne)
    elif userSelectItemOne == 5:
        priceOne = iceCream * userSelectAmountOne
        print("Ice Cream ",userSelectAmountOne,"X",iceCream,
              " = ",priceOne,"THB")
        itemOne = int(priceOne)
    print("DO you want something more? (Yes = 1 / No = 0)")
    userSelectProcessTwo = int(input(">>>  "))
    if userSelectProcessTwo == 1:
        print("Please choose number of a item which you want and amount")
        userSelectItemTwo = int(input("Item number : "))
        userSelectAmountTwo = int(input("Amount : "))
        if userSelectItemTwo == 1:
            priceTwo = coffee * userSelectAmountTwo
            print("Coffee ", userSelectAmountTwo, "X", coffee,
                  " = ", priceTwo, "THB")
            itemTwo = int(priceTwo)
        elif userSelectItemTwo == 2:
            priceTwo = friedRice * userSelectAmountTwo
            print("Fried rice ", userSelectAmountTwo, "X", friedRice,
                  " = ", priceTwo, "THB")
            itemTwo = int(priceTwo)
        elif userSelectItemTwo == 3:
            priceTwo = noodle * userSelectAmountTwo
            print("Noodle ", userSelectAmountTwo, "X", noodle,
                  " = ", priceTwo, "THB")
            itemTwo = int(priceTwo)
        elif userSelectItemTwo == 4:
            priceTwo = friedChicken * userSelectAmountTwo
            print("Fired Chicken ", userSelectAmountTwo, "X", friedChicken,
                  " = ", priceTwo, "THB")
            itemTwo = int(priceTwo)
        elif userSelectItemTwo == 5:
            priceTwo = iceCream * userSelectAmountTwo
            print("Ice Cream ", userSelectAmountTwo, "X", iceCream,
                  " = ", priceTwo, "THB")
            itemTwo = int(priceTwo)
        print("DO you want something more? (Yes = 1 / No = 0)")
        userSelectProcessThree = int(input(">>>  "))
        if userSelectProcessThree == 1:
            print("Please choose number of a item which you want and amount")
            userSelectItemTree = int(input("Item number : "))
            userSelectAmountTree = int(input("Amount : "))
            if userSelectItemTree == 1:
                priceThree = coffee * userSelectAmountTree
                print("Coffee ", userSelectAmountTree, "X", coffee,
                    " = ", priceThree, "THB")
                itemThree = int(priceThree)
            elif userSelectItemTree == 2:
                priceThree = friedRice * userSelectAmountTree
                print("Fried rice ", userSelectAmountTree, "X", friedRice,
                    " = ", priceThree, "THB")
                itemThree = int(priceThree)
            elif userSelectItemTree == 3:
                priceThree = noodle * userSelectAmountTree
                print("Noodle ", userSelectAmountTree, "X", noodle,
                    " = ", priceThree, "THB")
                itemThree = int(priceThree)
            elif userSelectItemTree == 4:
                priceThree = friedChicken * userSelectAmountTree
                print("Fired Chicken ", userSelectAmountTree, "X", friedChicken,
                    " = ", priceThree, "THB")
                itemThree = int(priceThree)
            elif userSelectItemTree == 5:
                priceThree = iceCream * userSelectAmountTree
                print("Ice Cream ", userSelectAmountTree, "X", iceCream,
                     " = ", priceThree, "THB")
                itemThree = int(priceThree)
            print("DO you want something more? (Yes = 1 / No = 0)")
            userSelectProcessFour = int(input(">>>  "))
            if userSelectProcessFour == 1:
                print("Please choose number of a item which you want and amount")
                userSelectItemFour = int(input("Item number : "))
                userSelectAmountFour = int(input("Amount : "))
                if userSelectItemFour == 1:
                    priceFour = coffee * userSelectAmountFour
                    print("Coffee ", userSelectAmountFour, "X", coffee,
                            " = ", priceFour, "THB")
                    itemFour = int(priceFour)
                elif userSelectItemFour == 2:
                    priceFour = friedRice * userSelectAmountFour
                    print("Fried rice ", userSelectAmountFour, "X", friedRice,
                            " = ", priceFour, "THB")
                    itemFour = int(priceFour)
                elif userSelectItemFour == 3:
                    priceFour = noodle * userSelectAmountFour
                    print("Noodle ", userSelectAmountFour, "X", noodle,
                            " = ", priceFour, "THB")
                    itemFour = int(priceFour)
                elif userSelectItemFour == 4:
                    priceFour = friedChicken * userSelectAmountFour
                    print("Fired Chicken ", userSelectAmountFour, "X", friedChicken,
                            " = ", priceFour, "THB")
                    itemFour = int(priceFour)
                elif userSelectItemFour == 5:
                    priceFour = iceCream * userSelectAmountFour
                    print("Ice Cream ", userSelectAmountFour, "X", iceCream,
                            " = ", priceFour, "THB")
                    itemFour = int(priceFour)
                print("DO you want something more? (Yes = 1 / No = 0)")
                userSelectProcessFive = int(input(">>>  "))
                if userSelectProcessFive == 1:
                    print("Please choose number of a item which you want and amount")
                    userSelectItemFive = int(input("Item number : "))
                    userSelectAmountFive = int(input("Amount : "))
                    if userSelectItemFive == 1:
                        priceFive = coffee * userSelectAmountFive
                        print("Coffee ", userSelectAmountFive, "X", coffee,
                              " = ", priceFive, "THB")
                        itemFive = int(priceFive)
                    elif userSelectItemFive == 2:
                        priceFive = friedRice * userSelectAmountFive
                        print("Fried rice ", userSelectAmountFive, "X", friedRice,
                              " = ", priceFive, "THB")
                        itemFive = int(priceFive)
                    elif userSelectItemFive == 3:
                        priceFive = noodle * userSelectAmountFive
                        print("Noodle ", userSelectAmountFive, "X", noodle,
                              " = ", priceFive, "THB")
                        itemFive = int(priceFive)
                    elif userSelectItemFive == 4:
                        priceFive = friedChicken * userSelectAmountFive
                        print("Fired Chicken ", userSelectAmountFive, "X", friedChicken,
                              " = ", priceFive, "THB")
                        itemFive = int(priceFive)
                    elif userSelectItemFive == 5:
                        priceFive = iceCream * userSelectAmountFive
                        print("Ice Cream ", userSelectAmountFive, "X", iceCream,
                              " = ", priceFive, "THB")
                        itemFive = int(priceFive)
                elif userSelectProcessFive == 0:
                    itemFive = 0
            elif userSelectProcessFour == 0:
                itemFour = 0
                itemFive = 0
        elif userSelectProcessThree == 0:
            itemThree = 0
            itemFour = 0
            itemFive = 0
    elif userSelectProcessTwo == 0:
        itemTwo = 0
        itemThree = 0
        itemFour = 0
        itemFive = 0
    print("---------------------------------")
    resalt = itemOne+itemTwo+itemThree+itemFour+itemFive
    print("Price       ","=  ",resalt,"THB")
    print("Vat         ","=  ","7%")
    print("Total price ","=  ",resalt*1.07,"THB")
    print("---------------------------------")
else:
    print("=== Please Try again ===")
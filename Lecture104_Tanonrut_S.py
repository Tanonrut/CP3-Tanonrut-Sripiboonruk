class Customer:
    name = ""
    lastName = ""
    age = 0
    def addCart(self):
        print("Added to ", self.name, self.lastName, "'s cart")

customer01 = Customer()
customer01.name = "Tanonrut"
customer01.lastName = "Siripiboonruk"
customer01.addCart()

customer02 = Customer()
customer02.name = "Nutchamon"
customer02.lastName = "Siripiboonruk"
customer02.addCart()

customer03 = Customer()
customer03.name = "Kunyar"
customer03.lastName = "Tangkamonwilart"
customer03.addCart()
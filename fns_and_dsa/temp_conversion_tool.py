class product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def value(self):
        return self.price * self.quantity
    
    def total_user_price(self, user_quantity):
        return self.price * user_quantity
    
product1 = product("pizza", 4000, 1000000)
product2 = product("burger", 2000, 10000000)
product3 = product("bread", 500, 10000000000)
product4 = product("sugar", 30000, 10000000)
product5 = product("bag", 1500, 100000000)
product6 = product("spaggetti", 400, 1000000)

print("available product:")
print("1 pizza")
print("2 burger")
print("3 bread")
print("4 sugar")
print("5 bag")
print("6 spaggetti")

choice = input("which product do you want to order?(1 to 6): ")

if choice == "1":
    quantity =  int(input("how many pizza do you want to buy?: "))
    result = product1.total_user_price(quantity)
    print(f"total price of {quantity} pizza: ${result}")
    
elif choice == "2":
    quantity = int(input("how many burger do you want to order?: "))
    result = product2.total_user_price(quantity)
    print(f"total price of {quantity} burger: ${result}")
    
elif choice == "3":
    quantity = int(input("how many bread do you want to order?: "))
    result = product3.total_user_price(quantity)
    print(f"total price of quantity{quantity} bread: ${result}")
    
elif choice == "4":
    quantity = int(input("how many sugar do you want to order?: "))
    result = product4.total_user_price(quantity)
    print(f"the total price for {quantity} sugar: ${result}")
    
elif choice == "5":
    quantity = int(input("how many bags do you want to order?: "))
    result = product5.total_user_price(quantity)
    print(f"the total price of bag is {quantity} bag: ${result}")
    
elif choice == "6":
    quantity = int(input("how amny spaggetti do you want to order?: "))
    result = product6.total_user_price(quantity)
    print(f"the total price of spaggetti is {quantity} spaggetti: ${result}")
else:
    print("credential attribute")
        

     
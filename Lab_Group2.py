'''
Created on Nov 1, 2023

@author: Group 2: Eric Arrigo, Malik Khan, Matteo Nobile, Benjamin Pierce, Mohammad Sarwar
This program presents a gift shop app for users/Fellowship of the Ring to shop at.
Customers have a running balance to shop with, and credit balance and inventory quantity
will update after every purchase.
If there are insufficient funds or inventory is depleted, customer/user will be notified.
'''
class Store:
    def __init__(self):    #initialize store's credit balances, inventory, and customers list
        self.inventory = []
        self.customers = []

    def toolMenu(self):    #display list of tools available for sale
        print("Gifts of Galadriel:")
        for i, tool in enumerate(self.inventory):
            print(f"{i + 1}. {tool['name']} - ${tool['price']} - In Stock: {tool['quantity']}")

    def toolSelection(self, choice):    
        try:
            choice = int(choice)
            if 1 <= choice <= len(self.inventory):
                tool = self.inventory[choice - 1]    #update quantity when a tool is purchased
                return tool['price'] * 1.0725    #include 7.25% CA sales tax to gouge customers
            else:
                print(f"{tool['name']} is out of stock. Cannot purchase anymore.")
                return 0  #return 0 for an out-of-stock numeric choice
        except ValueError:    #if input is not numeric, treat it as a tool name
            for tool in self.inventory:
                if tool['name'].lower() == choice.lower():
                    if tool['quantity'] > 0:
                        tool['quantity'] -= 1    #update quantity when a tool is purchased
                        return tool['price'] * 1.0725    #include 7.25% CA sales tax to gouge customers
                    else:
                        print(f"{tool['name']} is out of stock. Cannot purchase anymore.")
                        return 0    #return 0 for an out-of-stock tool name
            print("Invalid tool name. Please enter a valid tool name.")
            return 0    #return 0 for an invalid tool name

    def updateInventory(self, tool_index, quantity_sold):    #update quantity of a tool in the inventory post-sale
        tool = self.inventory[tool_index]
        tool['quantity'] -= quantity_sold

class Customer:
    def __init__(self, name, creditLimit):    #initialize name, credit limit, and credit balance
        self.name = name
        self.creditLimit = creditLimit
        self.creditBalance = creditLimit

    def displayCustomerInfo(self):    #display customer's information
        print(f"Customer Name: {self.name}")
        print(f"Credit Limit: ${self.creditLimit}")
        print(f"Credit Balance: ${self.creditBalance}")

    def makePurchase(self, totalCost):    #make purchase with available credit
        if totalCost <= self.creditBalance:
            self.creditBalance -= totalCost
            return True    #purchase successful
        else:
            print("Insufficient credit balance. Cannot complete the purchase.")
            return False  #insufficient credit balance

class Tool:
    def __init__(self, name, price, quantityInStock):    #initialize name, price, and quantity in stock
        self.name = name
        self.price = price
        self.quantityInStock = quantityInStock

    def displayToolInfo(self):    #display tool info
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Quantity in Stock: {self.quantityInStock}")

    def calculateTotalCost(self, quantityPurchased):    #calculate total cost of purchasing a certain quantity of the tool
        return self.price * quantityPurchased


if __name__ == "__main__":    #driver program
    my_store = Store()    #create instance of Store class

    #add tools to store's inventory
    my_store.inventory.append({"name": "Sheath", "price": 40.0, "quantity": 9})
    my_store.inventory.append({"name": "Belt", "price": 30.0, "quantity": 9})
    my_store.inventory.append({"name": "Cloak", "price": 60.0, "quantity": 9})
    my_store.inventory.append({"name": "Rope", "price": 50.0, "quantity": 1})
    my_store.inventory.append({"name": "Phial", "price": 100.0, "quantity": 1})

    my_customer = Customer("Frodo Baggins", 200.0)    #create instance of Customer class

    while True:    #continue making purchases until the user chooses to exit
        my_store.toolMenu()
        choice = input("Select a tool by number (type 'exit' to leave Lothlorien): ")
        if choice.lower() == 'exit':
            print("Good luck on your journey to Mordor.")
            break    #exit the loop if the user types 'exit'
        cost = my_store.toolSelection(choice)
        if cost > 0:
            print()    #empty line for readability
            print(f"Total cost: ${cost}")

            index = None

            try:
                choice = int(choice)
                if 1 <= choice <= len(my_store.inventory):
                    index = choice - 1
            except ValueError:
                pass

            if index is None:
                for i, tool in enumerate(my_store.inventory):
                    if tool['name'].lower() == choice.lower():
                        index = i
                        break

            if index is not None:
                quantity_to_sell = 1  #always subtract 1 from the inventory
                if my_customer.makePurchase(cost):    #update customer's credit balance
                    my_store.updateInventory(index, quantity_to_sell)  #update inventory after the tool is purchased
                    print(f"Purchase successful. Good luck on your journey to Mordor.")
                    print()  # Empty line for readability
                    my_customer.displayCustomerInfo()    #display customer's info, credit limit, and credit balance

        print("Updated Stock:")  # Display updated stock
        for tool in my_store.inventory:
            print(f"{tool['name']} - In Stock: {tool['quantity']}")
        print()    #empty line for readability
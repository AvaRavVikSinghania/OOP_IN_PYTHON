#Constructor is special method which will be called when we create a object
#inside that we create all the attribute
# method is function written inside the class
# Method and function calling way is not same
#special/magic/dunder methods (Any method start __ and end with __ called special method it predefined method)
#these magic method does not called by object it automatic  triggered
# user do not have any controlled on constructor
# so inside the constructor we do configuration related task like network connection in app
# self is basically current object

class Atm :

    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input(""" 
           Hello,how would you like to proceed?
           1.Enter 1 to create pin
           2.Enter 2 to deposit
           3.Enter 3 to withdraw
           4.Enter 4 to check balance
           5.Enter 5 to exit
       """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("exit")

    def create_pin(self):
        self.pin = input("Enter your pin")
        print("pin set successfully!")

    def deposit(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter the amount"))
            self.balance = self.balance + amount
            print("Deposit Successful")
        else:
            print("Invalid pin")
    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter the amount"))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("withdraw Successful")
            else:
                print("Not Enough amount")
        else:
            print("Invalid pin")

    def check_balance(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            print("Total balance",self.balance)
        else:
            print("Invalid pin")



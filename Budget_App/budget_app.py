# "STEP 1"
# Create a budget class that can instantiate objects based
# on different budget cateories like food, clothing, and entertainment.
 
class Budget:

    def __init__(self,name):
        self.name = name
        self.balance = 0

    #STEP 2
    #These object should allow for: 
    # 1. Depositing funds to each categories
    def deposit(self, amount):
        self.balance = amount

        return "Your new balance is $%s in %s budget." %(self.balance,self.name)

    # STEP 3
    # These objects should allow for: 
    # 2. Withdrawing funds from each category
    
    def withdraw(self, amount):
        if (self.balance < amount):
            return "Insufficient Funds"
        else:
            self.balance = self.balance - amount
            
            response = "*********************************\n"
            response += "Transaction Successful\n"
            response += "Your current balance is $%s in %s budget.\n" %(self.balance, self.name)

            return response
    
    # STEP 4
    # These objects should allow for:   
    # 3. Computing category balances.
    def compute_balance(self):
        response = "The balance for %s is $%s" %(self.name, self.balance)

        return response

    # STEP 5
    # These objects should allow for: 
    # 4. Transfering balance amounts between categories.
    def transfer(self, amount, category_transfer):    # caterogy is an object
        if self.name == category_transfer.name:
            response = "ERROR \n"
            response += "You cannot transfer within the same category"
            response += "you can only deposit within a category"

            return response        
        
        if self.balance < amount:
            return "Insufficient Funds"
        else:

            self.balance -= amount
            category_transfer.balance += amount

            response = "*************************************\n"
            response += "Transfer Successful\n"
            response += f"You've just transferred ${amount} to your {category_transfer.name} budget\n"
            response += f"The balance for {self.name} budget is ${self.balance}\n"
            response += f"The balance for {category_transfer.name} budget is {category_transfer.balance} \n" %()

            return response


food = Budget("food") # Instantiating objects from the class
clothing = Budget("clothing")
entertainment = Budget("entertainment")

# STEP 0

print("*********************WELCOME**************************\n")
print("%s budget has $%s balance" % (food.name, food.balance))
print("%s budget has $%s balance" % (clothing.name, clothing.balance))
print("%s budget has $%s balance \n" % (entertainment.name, entertainment.balance))

# STEP 1: Takes user input
print("*********************DEPOSIT***************************\n")
print(food.deposit(int(input("How much will you like budget for food?: "))))
print("***************************")
print(clothing.deposit(int(input("How much will you like to budget for clothing?: "))))
print("****************************")
print(entertainment.deposit(int(input("How much will you like to budget for Entertainment?: "))))
print("***************************\n")

# STEP 2
print("********************WITHDRAWAL************************\n")
print(food.withdraw(int(input("How much will you like to withdraw from food budget?: "))))
print("***************************")
print(clothing.withdraw(int(input("How much will you like to withdraw from clothing budget?: "))))
print("***************************")
print(entertainment.withdraw(int(input("How much will you like to withdraw from entertainment budget?: "))))
print("***************************\n")

# STEP 3
print("****************COMPUTE BALANCE*********************\n")
print(food.compute_balance())
print("***************************")
print(clothing.compute_balance())
print("***************************")
print(entertainment.compute_balance())
print("\n")

# STEP 4
print("*******************TRANSFER*************************\n")
print(clothing.transfer(50,entertainment))

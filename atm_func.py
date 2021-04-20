import random
from datetime import datetime

database = {}

now = datetime.now()
time = now.strftime('%X')
date = now.strftime('%d/%m/%y')

def init():

    print("Welcome to Tee Billions Bank")

    print("1. Login")
    print("2. Register")

    haveAccount = int(input("Please Select an option: \n"))

    if(haveAccount == 1):
            
        login()
    elif(haveAccount == 2):
           
        register()
    else:
        print("You have selected invalid option")  
        init()


def generateAccountNumber():
    
    return random.randrange(1111111111, 9999999999)

def login():
    print("-------------------LOGIN PAGE--------------------")
    print("Input your account details below")

    userAccount = int(input("What is your account number?: \n"))
    password = input("What is your password?:  \n")
    
    for accountNumber, userDetails in database.items():
        if(accountNumber == userAccount):
            if(userDetails[3] == password):
                bankOperations(userDetails) #calling bank operation inside login
        else:       
            print("Invalid account or password")
    login()


def register():
    print("---------------REGISTRATION PAGE-----------------")
    
    first_name = input("Enter your first name: \n")
    last_name = input("Enter your last name: \n")
    email = input("Enter your email address: \n")
    password = input("Create a password: \n")

    accountNumber = generateAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]

    print("Your Account Has been created")
    print("***************************************")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print("***************************************")
    
    login()


def bankOperations(user):
    print("-----------------BANK OPERATIONS-------------\n")
    
    print(f'Welcome %s %s, this login session is on {date} at {time}' % (user[0], user[1]))

    print('\nPlease select an option:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Logout')
    print('5. Exit')

    selectedOption = int(input('Please select an option:'))
            
    if(selectedOption == 1):
        print('you selected %s' % selectedOption)
        withdrawal()
                
    elif(selectedOption == 2):
        print('you selected %s' % selectedOption)
        cashDeposit()
                
    elif(selectedOption == 3):
        print('you selected %s' % selectedOption)
        complaint()

    elif(selectedOption == 4):
        logout() 

    elif(selectedOption == 5):
        exit()
    
    else:
        print('Invalid Option selected, please try again')
        bankOperations(user)

def withdrawal():
    cash = int(input('How much would you like to withdraw? \n'))
    print('Take your N%s' % cash)
    
def cashDeposit():
    deposit =int(input('How much would you like to deposit \n'))
    print('Your current balance is  %s' % deposit)
    
def complaint():
    input('What issue will you like to report? \n')
    print('Thank you for contacting us')
    

def logout():
    login()

init()
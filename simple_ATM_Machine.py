# ATM Machine

from datetime import datetime

name = input("What is your username? \n")
allowedUsers  = ['Seyi', 'Teju', 'Tee']
allowedPassword = ['PasswordSeyi', 'PasswordTeju', 'PasswordTee']
accountBalance = [10000, 80000, 50000]

#print(allowedUsers.index('Seyi'))

if(name in allowedUsers):
    password = input("Your password? \n")
    userId = allowedUsers.index(name)

    if(password == allowedPassword[userId]):
        print('Welcome %s' % name)

        now = datetime.now()
        time = now.strftime('%X')
        date = now.strftime('%d/%m/%y')
        print('Your current balance is  %s' % date, 'and' ,'Your current time is  %s' % time)

        print('these are the available options:')
        print('1. WIthdarwal')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectOption = int(input("Please select an option: \n"))
        if(selectOption == 1):
            cash = int(input('How much would you like to withdraw? \n'))
            
            if(cash > accountBalance[userId]):
                print('Insufficient Balance')
            else:
                print('Take your N%s' % cash)

        elif(selectOption == 2):
            deposit =int(input('How much would you like to deposit \n'))
            accountBalance[userId] += deposit
            print('Your current balance is  %s' % accountBalance[userId])

        elif(selectOption == 3):
            complaint = (input('What issue will you like to report? \n'))
            print('Thank you for contacting us')
        
        else:
            print('Invalid option selected, please try again')

    else:
        print('Password Incorrect, please try again')

else:
    print('Name not found, please try again')
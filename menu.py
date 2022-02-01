from bank import Bank

filibank = Bank()
def start_menu():
    print("Hi there, what would you like to do? \n"
          "1. Become a client at filibank \n"
          "2. Find a customer via the social security number \n"
          "3. Change your name \n"
          "4. Add a new account \n"
          "5. Close an account \n"
          "6. view all our clients! \n"
          "7  Remove a client due to terms of service violations \n"
          "8. Deposit :D \n"
          "9. Withdraw :( \n"
          "0. Log out and exit")
    option = int(input("Please select a option: "))

    if option == 1:
        pnr = input("Welcome please enter your social security number, 10 numbers please: ")
        if len(pnr) != 10:
            print("thats not a valid Social security number, 10 digits only")
            start_menu()
        else:
            fname = input("Please enter your first name: ")
            lname = input("please enter your last name:")
            filibank.add_customers(fname, lname, pnr)
            start_menu()

    elif option == 2:
        pnr =input("enter the Social security number of the customer your looking for,10 numbers please: ")
        if len(pnr) != 10:
            print("thats not a valid Social security number, 10 digits only")
            start_menu()
        else:
            customer = filibank.get_customer_with_pnr(pnr)
            print(customer)
            start_menu()

    elif option == 3:
        pnr = input("Welcome please enter your social security number, 10 numbers please: ")
        if len(pnr) != 10:
            print("thats not a valid Social security number, 10 digits only")
            start_menu()
        else:
            fname = input("please enter your first name: ")
            lname = input("please enter your last name: ")
            filibank.change_customer_name(fname,lname, pnr)
            start_menu()

    elif option == 4:
        pnr = input("Welcome please enter your social security number of the customer where you are trying to add a account, 10 numbers please: ")
        if len(pnr) != 10:
            print("thats not a valid Social security number, 10 digits only")
            start_menu()
        else:
            filibank.add_account(pnr)
            start_menu()

    elif option == 5:
        pnr = input("enter the Social security number of the customer your looking for,10 numbers please: ")
        if len(pnr) != 10:
            print("thats not a valid Social security number, 10 digits only")
            start_menu()
        else:
            account_nr = input("please enter the account you wish to close, make sure to write the correct number")
            filibank.close_account(pnr, account_nr)
            start_menu()

    elif option == 6:
        print("All our wonderful costumers: \n"
              f"{filibank.get_customers()}")
        start_menu()

    elif option == 7:
        pnr = input("enter the Social security number of the customer your looking to remove ,10 numbers please: ")
        if len(pnr) != 10:
            print("thats not a valid Social security number, 10 digits only")
            start_menu()
        else:
            remove = filibank.remove_customer(pnr)
            print(remove)
            start_menu()

    elif option == 8:
        pnr = input("enter the Social security number of the customer your looking to deposit to ,10 numbers please: ")
        if len(pnr) != 10:
            print("thats not a valid Social security number, 10 digits only")
            start_menu()
        elif len(pnr) == 10:
            account_nr= int(input("Enter the number of the account u wish to deposit to: "))
            money = int(input("How much money would you like to deposit: "))
            filibank.deposit(pnr,account_nr,money)
            start_menu()
        else:
            print("Whopsie something went wrong try again")
            start_menu()

    elif option == 9:
        pnr = input("enter the Social security number of the customer your looking to withdraw from ,10 numbers please: ")
        if len(pnr) != 10:
            print("thats not a valid Social security number, 10 digits only")
            start_menu()
        elif len(pnr) == 10:
            account_nr = int(input("Enter the number of the account u wish to withdraw from: "))
            money = int(input("How much money would you like to withdraw: "))
            filibank.withdraw(pnr, account_nr, money)
            start_menu()
        else:
            print("Whopsie something went wrong try again")
            start_menu()
    else:
        print("good day to you")
        start_menu()













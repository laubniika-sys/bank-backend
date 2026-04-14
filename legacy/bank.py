balance = 1000

euro = 1.17
real = 5.01
yen = 0.0063
pound = 1.34

print("Welcome to bank of Sasha!")

while True:
    print("\n1 - Balance")
    print("2 - Deposit")
    print("3 - Withdrawal")
    print("4 - Exit")

    try:
        option = int(input("Which option will you choose: "))
    except ValueError:
        print("Invalid digit: Please select a number.")
        continue

    if option == 1:
        print(f"Your balance is ${balance:.2f}")
    
    elif option == 2:
        print("1 - Deposit")
        print("2 - International Deposit")
        try:
            suboption = int(input("Which option: "))
        except ValueError:
            print("Invalid input!")
            continue
        if suboption == 1:
            try:
                deposit = float(input("How much dollars do you want to deposit: "))
            except ValueError:
                print("Invalid amount!")
                continue
            if deposit <= 0:
                print("Enter a valid amount!")
                continue
            balance += deposit
            print(f"Your balance is ${balance:.2f}")
        elif suboption == 2:
            print("1 - Euro")
            print("2 - Real")
            print("3 - Yen")
            print("4 - Pound")
            
            try:
                currency = int(input("Which currency will you choose: "))
            except ValueError:
                print("Invalid input!")
                continue
            rates = {1: ("euro", euro), 2: ("real", real), 3: ("Yen", yen), 4: ("Pound", pound)}

            if currency in rates:
                name, rate = rates[currency]
                try:
                    amount = float(input(f"How much {name} do you want to deposit: "))
                except ValueError:
                    print("Invalid amount!")
                    continue
                if amount <= 0:
                    print("Invalid amount!")
                    continue
                balance += amount * rate
                print(f"Your balance is ${balance:.2f}")
            else:
                print("Invalid currency option")

    elif option == 3:
        try:
            withdrawal = float(input("How much would you like to withdraw: "))
            if withdrawal > balance:
                print("Insufficient funds")
            else:
                balance -= withdrawal
                print(f"Your balance is ${balance:.2f}")
        except ValueError:
            print("Invalid input!")

    elif option == 4:
        print("Thanks for using Bank of Sasha!")
        break

    else:
        print("Please! Select a valid operator")
        

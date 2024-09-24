
# Project on ATM


passcode = 6646

def passcode_check():
    counter = 0

    while counter < 3:
        value = (int(input("Enter Your Passcode: ")))

        if value == passcode:
            print("Your Passcode is Correct")
            return True
        else:
            print("Entered incorrect passcode, Try Again")
            counter = counter + 1
            if counter == 3:
                print("Max limit is reached, Try again after 30 min.")
                return False

def main():
    acc_balance = 0
    user = True
    if passcode_check() is True:
        while user is True:
            withdraw_or_deposit = str(input("Would you like to withdraw or deposit (Enter W/D/Cancel)? :"))
            action = withdraw_or_deposit.lower()
            if action == "d":
                amount = int(input("Enter amount to deposit: "))
                acc_balance += amount
                print("Your Current Balance is " + str(acc_balance))
                user = True

            if action == "w":
                amount = int(input("Enter amount to withdraw: "))
                acc_balance -= amount
                print("Your Current Balance is " + str(acc_balance))
                user = True

            if action == "c" or action == "cancel":
                print("Thank You, Visit again")
                user = False




main()






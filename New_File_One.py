# Project on ATM

PIN = 6646
def pin_check():
    counter = 0
    print("Welcome to ABC Bank")
    while counter < 3:
        value = (int(input("Enter Your PIN: ")))
        length = len(str(value))
        if length == 4:
            print("Your Passcode is Correct")
            return True
        else:
            print("Entered PIN is incorrect")
            print("Enter a 4 digit PIN")
            counter = counter + 1
            if counter == 3:
                print("Max limit is reached, Try again after 30 min.")
                return False

def main():
    acc_balance = 0
    user = True
    if pin_check() is True:
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
                if amount <= acc_balance:
                    acc_balance -= amount
                    print("Your Current Balance is " + str(acc_balance))
                    user = True
                else:
                    print("Insufficient Balance")
                    user = True

            if action == "c" or action == "cancel":
                print("Thank You, Visit again")
                user = False
main()






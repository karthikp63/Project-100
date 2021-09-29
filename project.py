class atm(object):
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number
    def CashWithdrawel(self, amount):
        new_amount = 50000 - amount
        print("you have withdrawen this amount of cash: " + str(amount) + ". Your remaining balance is now : " + str(new_amount) )
    def BalanceEnquiry(self):
        print("Your balance is 50000 ")
def main():
    card_number = input("Insert your card number here: ")
    pin_number = input("Insert your pin number here: ")
    new_user = atm(card_number, pin_number)
    print("Choose your activity")
    print("1. BalanceEnquiry 2. Withdrawel")
    activity = int(input("Enter Activity Number: "))
    if(activity == 1):
        new_user.BalanceEnquiry()
    elif(activity == 2):
        amount2 = int(input("Enter The Amount: "))
        new_user.CashWithdrawel(amount2)
    else:
        print("Enter a valid number!")

if __name__ == "__main__":
    main()
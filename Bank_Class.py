import random
class Bank:
    Bank_name="Bank Of Maharashtra"
    Branch="Balewadi Pune"
    AC_no=random.randint(1,100)
    org_amount=0
    def __init__(self,name,initial_bal):
        self.name=name
        self.initial_bal=initial_bal
        Bank.org_amount=initial_bal
        print("Account Created...")
        print("Holder NAME :",self.name)
        print("BANK NAME :",Bank.Bank_name)
        print("Branch Name :",Bank.Branch)
        print("Account Number :",Bank.AC_no)
        print("Initial Balance :",Bank.org_amount)
        
    def get_details(self,account_num):
        self.account_num=account_num
        if(Bank.AC_no==account_num):
            print("Holder NAME :",self.name)
            print("Bank NAME :",Bank.Bank_name)
            print("Branch Name:",Bank.Branch)
            print("Account Number:",Bank.AC_no)
            print("Total Balance :",Bank.org_amount)
    def Deposite(self,acc_no):
        amount=int(input("Enter The Amount That You Want To deposite"))
        if(Bank.AC_no==acc_no):
            Bank.org_amount+=amount
            print("Deposite Successfully,,,")
    def Withdraw(self,acc_no):
        amount=int(input("Enter The Amount That You Want To Withdraw"))
        if(Bank.AC_no==acc_no):
            Bank.org_amount-=amount
            print("Withdraw Successfully,,,")
            
name=input("Enter The Name :")
initial_amount=int(input("Enter The Initial Amount :"))
b1=Bank(name,initial_amount)
while True:
    choice=int(input("\nEnter The Choice \n1.Deposite\n2.Withdraw\n3.Display_details\n4.Exit\n"))
    match choice:
        case 1:
            acc=int(input("Enter The Account Number:"))
            b1.Deposite(acc)
        case 2 :
            acc=int(input("Enter The Account Number:"))
            b1.Withdraw(acc)
        case 3 :
            acc=int(input("Enter The Account Number:"))
            b1.get_details(acc)
        case 4:
            break

            

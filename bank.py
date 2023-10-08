
org_account_num = 0
name=0
mobile=0
org_amount=0
def create(acc_no,name,mobile):
    print("Account Has been created successfully..,.,.")
    org_account_num = acc_no
    name = name
    mobile=mobile
    return acc_no,name,mobile

def credit(acc_no,amount):
    if(acc_no==org_account_num):
        org_amount=org_amount+amount
        return org_account_num
    else:
        print("Provide Valid Account Number .,.,.,.,.")
def debit(acc_no,amount):
    if(acc_no==org_account_num):
        org_amount=org_amount-amount
        return org_account_num
    else:
        print("Provide Valid Account Number .,.,.,.,.")
def check_balance(acc_no):
    if(acc_no==org_account_num):
        print("Your Account Balance Is :",org_amount)
        return org_amount
    else:
        print("Provide Valid Account Number .,.,.,.,.")

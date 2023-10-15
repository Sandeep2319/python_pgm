org_amount=0

def create(acc_no,name,mobile):
    print("Account Has been created successfully..,.,.")
    global org_account_num 
    org_account_num= acc_no
    global name1
    name1= name
    global mobile1
    mobile1=mobile
    return acc_no,name,mobile

def credit(acc_no,amount):
    if(acc_no==org_account_num):
        global org_amount
        org_amount=org_amount + amount
        return org_account_num
    else:
        print("Provide Valid Account Number .,.,.,.,.")
def debit(acc_no,amount):
    if(acc_no==org_account_num):
        global org_amount
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

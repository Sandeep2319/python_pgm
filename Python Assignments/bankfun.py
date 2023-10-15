from bank import *

while True:
    n=int(input("Enter The Input below >> \n1.Create Account\n2.Credit Balance\n3.Debit Balance\n4.available balance\n5.exit\n"))
    match n:
        case 1:
            ac_no=int(input("Enter The Account_Number :"))
            name=input("Enter The Name :")
            mo=int(input("Enter The Mobile Number :"))
            create(ac_no,name,mo)
            
        case 2:
             ac_no=int(input("Enter The Account_Number :"))
             amount=int(input("Enter The amount :"))
             credit(ac_no,amount)
             
        case 3:
             ac_no=int(input("Enter The Account_Number :"))
             amount=int(input("Enter The amount  :"))
             debit(ac_no,amount)
             
        case 4:
             ac_no=int(input("Enter The Account_Number :"))
             check_balance(ac_no)
             
        case 5:
            print("Exit Successfully")
            break
            
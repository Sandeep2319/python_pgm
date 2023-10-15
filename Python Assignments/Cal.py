def calculator():
    ch=int(input())
    
    if(ch == 1):
        num1=int(input("Enter the first number: "))
        num2=int(input("Enter the second number: "))
        print(num1+num2)
        
    if(ch == 2):
        num1=int(input("Enter the number: "))
        print(num1*num1)
        
    if(ch == 3):
        num1=int(input("Enter the first number: "))
        num2=int(input("Enter the second number: "))
        print(num1**num2)
        

while True : 
    print("Menu: ")
    print("What operation do you want to do: ")
    print(f"\n1.Addition\n 2.Square\n 3.Exponential\n")
    calculator()
    
    ch =int(input("do you wish to continue press 0: "))
    if ch==0:
        break
        
    

    

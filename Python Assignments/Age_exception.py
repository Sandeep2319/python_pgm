def Age(age):
    if (age > 10000) :
        raise Exception
   
try :
    age = int(input("Enter the user age: "))
    if (age < 10000):
        age = int(input("Enter the user age again: "))
    Age(age)
    
except Exception:
    print("You have lived more than 100001 days")


        

    
    



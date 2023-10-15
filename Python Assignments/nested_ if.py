count = 2
while (count > 0):

        num = int(input("Enter an number: "))
        count = count - 1 
        
        if num % 3 == 0 and num %5 == 0 :
            print ("fizz buzz")
        elif  num % 2 == 0 and num % 4 == 0 :
            print ("buzz")
            

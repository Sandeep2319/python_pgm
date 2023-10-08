#Factorial of number using recursive  
def function(num):
    if(num==0):
       return 1
    else:
         return function(num-1)*num
     
     
fo= int(input("Enter a number : "))
print ("Factorial of number is: ", function(fo))
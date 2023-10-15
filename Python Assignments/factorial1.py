#Factorial of number using recursive  
def function(fo):
    if(fo==0):
       return 1
    else:
         return function(fo-1)*fo
     
     
fo= int(input("Enter a number : "))
print ("Factorial of number is: ", function(fo))
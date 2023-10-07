
'''
def add_number(num1,num2):
    sum = num1 + num2
    return sum
print (add_number(1,2))

def multiply(num1,num2):
    mul = num1 *num2
    if mul>2:
        print (mul)
    else:
        print ("small no")
    return mul
print (multiply(1,2))
'''
'''
#list (list are mutable)
ls = [1,2,3,4]
ls[2] = 100
print (ls)


# dictionary (These are mutable)
dict = {1: "one",
        2: "two",
        3: "three"}

print (dict[1])

#tuples 

tuple = (1,2,3,4)
print (tuple)


#implicit typecasting 
var1 =1
var2 =1.0
print (type(var2))
print (var1==var2)
'''

var3  = input("Enter a number: ")
print(var3)
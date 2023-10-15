def dict():
    dict={}
    ele=int(input("Enter the no u want to insert: "))
    for i in range(0,ele):
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        dict[key] = value
    return dict


def  tuple1():
    tuple2=()
    ele=int(input("Enter the no u want to insert: "))
    for i in range(0,ele):
        # key = input("Enter the key: ")
        value = input("Enter the value for tuple seprated by comma: ").split(",")
    return tuple2 
    
d={}

no_of_item=int(input("Enter the no of elements do u want to add: "))

for i in range(0,no_of_item):
    keys = input("Enter the key: ")
    t = input("Enter the datatype u want to add: ")
    if(t == 'int'):
        values = int(input("Enter the value: "))
        d [keys] = values
    elif(t == 'float'):
        values = float(input("Enter the value: "))
        d [keys] = values
    elif(t == 'str'):
        values = int(input("Enter the value: "))
        d [keys] = values
    elif(t == 'dict'):
        d[keys] = dict()
    elif(t == 'tuple'):
        d [keys] = tuple1()
    
#Calling dictionary here!     
print(d)

                
                
            
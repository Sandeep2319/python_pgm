"""
    1) Create a postive numbered list 
    Note : raise an exception if the users inserts a negative number OR user creates an empty list 
    2) Create a negative  numbered list 
    Note : raise an exception if the users inserts a positive number/Zero OR user creates an empty list
    3) Create a heterogenous list 
    Note : raise an exception if the users creates a homogenous list (all elements of same datatype)

    4) Check if the element is present in the list 
    Take the Input element that you would like to search
    and which of the above three list that he want to search element from
    Note : raise an exception if the element is not found in the list
    with a message "Sorry, Element could not be found"
        
    5) Refresh the program to start with blank lists
    6) Exit

"""

def fun_1():
    list1=[]
    el=int(input("How many element want to insert ?? :"))
    for i in range(el):
        a=(input("Enter  value: "))
        list1.append(a)
    return list1  
while True:
    n=int(input("Enter The Input below >> \n1.Create Positive Number List\n2.Create a negative  numbered list \n3.Create a heterogenous list\n4Create a Homogenous list.\n5.Check if the element is present in the list\n6.Refresh the program to start with blank lists\n7.exit\n"))
    match n:
        case 1:
            try:
                li=fun_1()
                for i in range(len(li)):
                    if( li[i] < 0):
                        raise Exception
            except Exception:
                print("Please Enter Positive values.....")
                fun_1()
        case 2:
            try:
                li=fun_1()
                for i in range(len(li)):
                    if( li[i] >0):
                        raise Exception
            except Exception:
                print("Please Enter Negative values.....")
                fun_1()
        case 3:
            try:
                li=fun_1()
                print(li)
                for i in range(len(li)):
                    if( type(li[i] ) == type(li[i+1])):
                        raise Exception
            except Exception:
                print("Please Enter Heterogenous  values.....")
                fun_1()
            
        case 4:
            try:
                
                li=fun_1()
                print(li)
                for i in range(len(li)):
                    if( type(li[i] ) != type(li[i+1])):
                        raise Exception
            except Exception:
                print("Please Enter  homogenous values.....")
                fun_1()
        case 5 :
            try:  
                
                li=fun_1()
                for i in range(li):
                    if in_ == li[i] :
                        print("element is present :",li[i])
                raise Exception
            except Exception:
                print("Value Not Present//.....")
                
                fun_1()
            
        case 6:
            li=fun_1()
            del li
            print(li)
        case 7:
                break
            



# Exercise 1 : Create a dictionary like this by taking values from the user:

# {
# 'employee_id' : 1,
# 'employee_name' : 'Sarwesh'
# 'account_number' : 829389283982839,
# 'salary' : 1000.99999,
# 'address' : {' address' : 'Pune' , 'work_address' : 'mumbai'} ,
# 'awards': ['employeeOfTheYear','StarOfTheMonth']
# 'subjects_enrolled' : ('Physics','Chemistry')
# }

# def dict_fun(d):
    
    
def my_dict():
    dict2={}
    ele=int(input("How Much Element Do you want to insert in dictionary ??"))
    for i in range(ele):
        keys=input("Enter the  keys for dictionary: ")
        values=input("Enter the  values for dictionary:")
        # d1[keys[i]] = values[i]
        dict2[keys]=values
        # d1|=dict2
    return dict2
def my_list():
    dict3=[]
    ele=input("How Much Element Do you want to insert in list ??")
    for i in range(ele):
        keys=input("Enter the  keys for list: ")
        values=input("Enter the  values for list:")
        dict3[keys]=values
        # d1|=dict2 
    return dict3
def my_tuple():
    tup1=()
    ele=input("How Much Element Do you want to insert in tuple ??")
    for i in range(ele):
        keys=input("Enter the  keys for list: ")
        values=input("Enter the  values for list:")
        tup1[keys]=values
        # d1|=dict2 
    return tup1
d1={}
no_of_item=int(input("Enter the no of item u want to add: "))
for i in range(0,no_of_item,1):
    keys=input("Enter the  keys: ")
    v=input("Which type of value do you want to insert ")
    if(v=='int'):
        values=int(input("Enter the  values: "))
        d1[keys] = values
    elif(v=='float'):
        values=float(input("Enter the  values: "))
        d1[keys] = values
    elif(v=='str'):
        values=input("Enter the  values: ")
        d1[keys] = values
    elif(v=='dict'):
        d1[keys]=my_dict()
    elif(v=='list'):
        d1[keys]=my_list()
print(d1)


    



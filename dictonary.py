# dict1 ={1:"sandeep",2:"Rachna",3:"suraj"}
# dict1[4] = {4: "sandeep"}
# print(dict1.values())
# print (dict1.get(2))

# for key in dict1.keys():
#     print (f'the keys is: {key}')
    
# for values in dict1.values():
#     print (f'the values is: {values}')

# del d


#crud oPERAITON 

# d = dict([(1,"one"),(2,"two")])
# print(d)

# # DEMO CRUD Operations on Dictionary 

# 1 : creating a dictionary 
# d = {'name': 'Gaurav' , 'rollno' : 1 ,'rollno' : 2}
# print(d)

# #by using list to create dictiomnary
# d= dict(name = 'sagar', surname = 'narvade')
# print (d)

# # by using list we create dictionary
# d = dict ([('name', 'sandeep'), ('surname ', 'narvade')])
# print (d)


# 1 : creating a empty dictionary and adding a values 

# d={}
# keys=[1,2,3]
# values=['sandeep','saloni','shradhha']

# for i in range(0,len(keys)):
#     d[keys[i]] = values[i]
    
# print (d)

# d={}
# no_of_items=int(input("Enter the no of item you want to add: "))


# for i in range (0,no_of_items,1):
#     keys = int(input("Enter the keys: "))
#     values = input("Enter the values: ")
#     d[keys] = values

# print(d)

# d={}
# no_of_item=int(input("Enter the no of item u want to add: "))

# for i in range(0,no_of_item,1):
#     keys= int(input("Enter the number of keys: "))
#     values=input("Enter the number of values: ")
    
#     d[keys] = values 
# print (d)

dict ={1:'sandeep'}

print("The roll number is: ",dict[1])
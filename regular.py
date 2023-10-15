import re
string0 = "gaurav1234@gmail.com"
string1 = "pratik190900234@gmail.com"
string2 = "2009_rocking_person@yahoo.com"
string3 = "GodFather2022@yahoo.com"
string4 = "Brocklesner_89_WWE@yahoo.com"
string5 = "TheRock_WWE@yahoo.com"
string6 = "JohnCena_WWE@yahoo.com"
string7 = "Undertaker_Roman_reigns@outlook.com"
string8 = "6789764666@rediffmail.com"
string9 = "Kane#6789@gmail.com"
string10 ="2009_Person@yahoo.com"


my_list = [string0,string1,string2,string3,string4,string5,string6,string7,string8,string9,string10]

#1)provide me the list of emails that do have special characters of #~`!
for test in my_list:
    result = re.search("^[a-zA-Z0-9#~`!]+@[a-zA-Z0-9]+\.[a-zA-Z]+$", test)  
    if result :
        print(f"{test}\n")
print("**************************************************")
# #2) provide me the list of emails that start with numbers
for test in my_list:
    result = re.search("^[0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+$", test)
    if result :
        print(f"{test}")
print("**************************************************")    
# 3) provide me the list of emails that start with numbers followed by an underscore

for test in my_list:
    result = re.search("^[0-9]+[_]+.*", test)
    if result :
        print(f"{test}")
print("**************************************************")           
#4) provide me the list of emails that start with numbers followed by an underscore or small case characters

for test in my_list:
    result = re.search("^[0-9]+[_]+[a-z]+.*", test)
    if result :
        print(f"{test}")
        
print("**************************************************") 

#5) provide me the list of emails that start with numbers followed by an underscore or small case characters or large case characters
for test in my_list:
    result = re.search("^[0-9]+[_]+[a-zA-Z]+.*", test)
    if result :
        print(f"{test}")
        
print("**************************************************")  

#6) Provide me list of emails with only numbers before the @
for test in my_list:
    result = re.search("^[a-zA-Z]+[0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+$", test)
    if result :
        print(f"{test}")
print("**************************************************")  

#7) Provide me list of emails with numbers anywhere before the @

for test in my_list:
    result = re.search("^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+$", test)
    if result :
        print(f"{test}")
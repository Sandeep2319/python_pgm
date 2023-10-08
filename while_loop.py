# count = 2
# while (count > 0):

#         num = int(input("Enter an number: "))
#         count = count - 1 
        
#         if num % 3 == 0 and num %5 == 0 :
#             print ("fizz buzz")
#         elif  num % 2 == 0 and num % 4 == 0 :
#             print ("buzz")

# # to display a range using range keyword       
# print(list(range(1,5,1)))

#to itrate through a string 
# name = "sandeep"
# for character in name:
#     print (character)



num=1 
while (num<10):
    if num <6:
        print ("run")
        num+=1
        continue
    num+=1
    print (num, end=" ")
    
    continue
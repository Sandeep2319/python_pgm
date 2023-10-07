no=int(input("Enter The Number : "))
temp=no
rem=1
sum=0
while (no > 0):
    rem=no%10 # 121 ,,1,2,1
    sum=(sum*10)+rem # 1,12,121
    no=no//10 # 12,1
print(sum)
if (temp==sum):
    print("Number is palindrome...")
else :
    print("Not Palindrome Number..")
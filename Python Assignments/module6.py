src = input("Enter the source: ")
dest= input("Enter the destination: ")
fare = int(input("Enter the faare: "))
discount =int(input("Enter the discount:"))

dis=fare-discount/100*fare

print (f"fare from {src} to {dest} is {fare} INR with has a discount of {dis}")
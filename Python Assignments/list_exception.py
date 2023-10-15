def list1(a):
    list2=[10,20,30,40,50]
    
    for i  in range(0,len(list2),1):
        if a == i:
            print("Location  is present")
            return list2[i]
    raise IndexError
try:
    a=int(input("Enter the location at which you want a Data ? : "))
    print(list1(a))
except IndexError:
    a=int(input("Index error please enter again,,,: "))
    print(list1(a))

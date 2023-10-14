
def set_union(setA,setB):
    setA=setA.union(setB)
    return setA
def set_intersection(setA,setB) :
    setA=setA.intersection(setB)
    return setA
def set_minus(setA,setB) :
     setA.difference(setB)
     return setA
def is_member_of_set(setA,setB) :
    v=input("Enter The Value :")
    if(v in setA):
        print("It is a member of setA")
    elif(v in setB):
        print("It is a member of setB")
    return "Done..."
def set_display(setA):
    lens=len(setA)
    return lens
def set_display(setB):
    lens=len(setB)
    return lens
def set_add_element(setA):
    value=input("Enter The Value ")
    setA.add(value)
    return setA
def set_add_elements(setA):
    value=input("Enter The Value ").split(",")
    setA.update(value)
    return setA
def set_remove_element(setA):
    setA.pop()
    return setA
# def set_remove_element(setA):
# 	setA.pop() 
#     return setA

setA=set(input("Enter The Set A : ?").split(","))
setB=set(input("Enter The Set B : ?").split(","))

while True:
    n=int(input("Enter The Options \n1.Union\n2.Intersection\n3.A-B\n4.B-A\n5.Take a element from user and Display if that element is a member of set B\n6. Display number of elements in the set A\n7.Display number of elements in the set B\n8.Add an element taken from the user to the set A\n9.Add multiple elements taken from the user to the set A\n10.Remove an element taken from the user from set A\n11.exit\n"))

    match n :
        case 1 :
            
            a=set_union(setA,setB) 
            print(a)
        case 2 :
            a=set_intersection(setA,setB)
            print(a)
        case 3 :
            a=set_minus(setA,setB)
            print(a)
        case 4:
             a=set_minus(setA,setB)
             print(a)      
        case 5 :
            a=is_member_of_set(setA,setB)
            print(a)
        case 6 :
            a=set_display(setA)
            print(a)
        case 7 :
            a=set_display(setB)
            print(a)
        case 8:
            a=set_add_element(setA)
            print(a)
        case 9 :
            a=set_add_elements(setA)
            print(a)
        case 10 :
            a=set_remove_element(setA)
            print(a)
        case 11 :
            break

def add_ele(list1):
    str=input("Enter the string: ")
    list1.append(str)

def display(list1):
    print(list1)
    
def add_multiple(list1):    
    str=input("Enter the string comma seprated: ").split(",")
    list1.append(str)
    
def remove_ele(list1):
    ele=input("Enter the nam you want to delete: ")
    list1.remove(ele)

def remove_last(list1):
    list1.pop()

def store():
    list1 = input('for ex: Pratiksha, Kevin, Sachin, Yuvraj, Sania \n').split(",")
    while True :
        n = int(input("Enter the choice:\n 1.Add element\n 2.display\n 3.Add multiple element\n 4.Remove element\n 5.Remove last element\n 6.Exit\n"))
        match n:
            case 1: 
                add_ele(list1)
            case 2 :
                display(list1)
            case 3:
                add_multiple(list1)
            case 4:
                remove_ele(list1)
                
            case 5:
                remove_last(list1)
            case 6:
                break
            
store()
            
                
    
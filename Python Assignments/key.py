def Dict(a):
    d={1:"red",2:"blue",3:"Orange"}
    if a in d:
        print("Key is present")
        print(d.get(a))
    else:
        raise KeyError
try:
    a=int(input("Enter the key: "))
    Dict(a)
except ValueError:
    a=int(input("value error please enter again,,,: "))
    Dict(a)
except KeyError:
    a=int(input("key is not found & please enter again,,,: "))
    Dict(a)

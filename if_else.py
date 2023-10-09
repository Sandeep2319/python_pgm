def fun(weather,pref):   
    if weather == "cold":
        if pref == "hot":
            print ("I am having hot tea")    
        else:
            print ("I am having water")
        
    if weather == "sunny":
        if pref == "hot":
            print ("I am having hot tea")    
        else:
            print ("I am having water")
    
global weather  
global pref 
        
wea = True
while (wea==True):
    weather= str(input("Enter the weather: "))
    pref=str(input("enter a perf"))
    fun(weather,pref)
    wea=int(input("do you wish to continue 0 to skip"))
    if wea== 0:
        wea = False

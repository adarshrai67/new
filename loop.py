def nameList(list): 
    for i in name: print(i)
    print()

def nameChar(name):
    for i in name: print (i)
    print()

def forTable(value):
    for i in range(1,11): print(i*value)
    print()

def whileTable(value):
    count = 0
    while (count < 11): 
        print(count*value)
        count=count+1
    print()
    
def oddEven():    
    count = 0
    while (count < 11):
        if(count == 0): print(f"{count} = neither even nor odd")
        elif(count % 2 == 0): print(f"{count} = even")
        else: print(f"{count} = odd")
        count += 1
    print()

def prime():
    i = 2
    while (i < 100):
        j=2
        while(j <= (i/j)):
            if not(i%j): break
            j += 1
            if (j > (i/j)): print(i," is prime")
        i +=1
    print()
    
def passBreak(list):    
    for i in list:
        if(i == 5): pass
        elif(i == 67): break
        else: print(i)

name = ["adarsh", "vandana", "abhishek"]
nameList(name)
nameChar(name[1])
forTable(7)
whileTable(10)
oddEven()
prime()
list = [7,6,5,676,76,67,100]
passBreak(list)
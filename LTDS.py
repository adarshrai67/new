list = ["Adarsh", "Vandana", "Abhishek"]
list1 = [6,7,67,76]
tuple = ("adarsh", "vandana", "abhishek")
dict = {"name" : "adarsh", "roll" : 22210}
set = {"ADARSH", "VANDANA", "ABHISHEK"}
print(list,"\n",tuple,"\n",dict,"\n",set)


print (len(list))
print (sum(list1)/len(list1))
list1.append(5)
print(list1)
list1.sort()
print(list1)
list1.remove(5)
print (list1)
list1.clear()
print(list1)


print("\n",type(set))
for i in set:
    print(i)
    
    

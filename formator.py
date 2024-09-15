firstName = input("first name : ")
middleName = input("middle name : ")
lastName = input("last name : ")
fullName = "{} {} {}".format(firstName, middleName, lastName)
print ("Full Name : ", fullName)
age = int(input("age : "))
branch = input("branch : ")
detail = "{} {} {}".format(fullName, age, branch) 
print("Detail : ", detail)
print("{4} {1} {0} {2} {3}".format(firstName, middleName, lastName, age, branch)) 

print(firstName, middleName, lastName, age, branch, sep=" --- ")


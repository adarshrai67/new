class Person:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
    
    def show(self):
        print("Name : ", self.name, "\nSex : ", self.sex, "\nAge : ",self.age)
    
p1 = Person("Vandana", "Female", "21")
p2 = Person("Adarsh", "Male", "21")
p1.show()
print()
p2.show()
    
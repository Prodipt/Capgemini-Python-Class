
# Inheritence

# class kapdo:
#     def __init__(self, color, type):
#         self.color = color
#         self.type = type
    
#     def info(self):
#         print(self.color, self.type)

# class dukan1(kapdo):
#     def xyz(self):
#         print("self service")



# d = dukan1("pink","Tanki")
# d.info()


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def info(self):
#         print("Name of Manager : ", self.name)
#         print("Salary of Manager : ", self.salary)


# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department

#     def whichdept(self):
#         print("Deapartment Name: ", self.department)

#     @property
#     def okok(self):
#         print("Happy IDK!!!")


# M1 = Manager("ABC", 2000, "CSE")
# M1.info()
# M1.whichdept()
# M1.okok



# class Circle:
#     def __init__(self):
#         self.radius = int(input("Enter the radius: "))
#         print(f"Radius Of Circle : {self.radius}")

#     def area(self):
#         print("Area of Circle : ", (3.14)*self.radius*self.radius)

#     @property  
#     def circumference(self):
#         print("Circumference of Circle : ", 2*(3.14)*self.radius)

# c1 = Circle()
# c1.area()
# c1.circumference


# Lambda , Map  FIlter, Filter
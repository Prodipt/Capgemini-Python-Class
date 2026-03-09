# # 'Date - 9th March 2026'

class College:
    c_name = 'JECRC'
    loc = 'Jaipur'

    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age


# s1 = College()

# print(College)
# print(s1)
# print(s1.c_name)
# print(s1.loc)

# s1.name = 'Pradipt Prasoon'

# print(s1.name)

# s2 = College
# print(s2.name)

class Corporate:
    Company = 'XYZ'
    networth = 100000
    started = "9thMarch"

    def __init__(self, id, branch, qualification):
        self.id = id
        self.branch = branch
        self.qualification = qualification

    def display(self):
        print(self.id, self.branch, self.qualification)

# E1 = Corporate
# E1.id = 101
# E1.branch = 'SE'
# E1.qualification = 'Btech-AI/ML'

# E2 = Corporate
# E2.id = 202
# E2.branch = 'SE'
# E2.qualification = 'Btech-Electrical'


# E3 = Corporate
# E3.id = 303
# E3.branch = 'SDE'
# E3.qualification = 'Btech-CS'


# print("Employee 1 Details:")
# print(E1.id)
# print(E1.branch)
# print(E1.qualification)

# print("\nEmployee 2 Details:")
# print(E2.id)
# print(E2.branch)
# print(E2.qualification)

# print("\nEmployee 3 Details:")
# print(E3.id)
# print(E3.branch)
# print(E3.qualification)

E4=Corporate(404, "Tester", "Python")
E5=Corporate(505, "Trainee", "Python")
E4.display()
E5.display()
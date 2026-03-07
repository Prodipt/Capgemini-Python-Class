# def form(n,m,a,p):
#     print("Name =",n, "Mail =",m, "Age =",a, "Phone =",p)

# form("pra", "@", 7, 9876)
    
# def form2(n,m,a,p=11):
#     print("Name =",n, "Mail =",m, "Age =",a, "Phone =",p)

# form2("pra", "@", 7)


    
# def form2(n,m,a,p=11,s = None):
#     print("Name =",n, "Mail =",m, "Age =",a, "Phone =",p, "S_no =" ,s)

# form2("pra", "@", 7, 789 )


# def form2(n,m,a,p=11,s = None):
#     print("Name =",n, "Mail =",m, "Age =",a, "Phone =",p, "S_no =" ,s)

# form2("pra", "@", 7, s=789 )


# def form2(*a):
#     print('a:', a)
#     print(len(a))

# form2("pra", "@", 7, 789 )


# def form3(**a):
#     print('a:', a)
#     print(len(a))

# form3(x="pra", y= "@", z=7, aa=789 )



# def form3(**a):
#     print('a:', a)
#     print(len(a))

# form3(Name="pra", Email= "@", Age=7, Ph_num=789 )


Name = input("Enter Name: ")

Email = input("Enter Email: ")

Age = int(input("Age : "))

Ph_num = int(input("Ph_num : "))

def form4(**A):
    print("INFO: ", A)
    print(len(A))

form4(Name = Name, Email=Email, Age=Age, Ph_num=Ph_num)

'''
Different Types of Parameters in Python Functions

1️⃣ Positional Parameters

Values are passed based on position/order.

def add(a, b):
    print(a + b)

add(5, 3)

2️⃣ Keyword Parameters

Arguments are passed using parameter names.

def info(name, age):
    print(name, age)

info(age=21, name="Pradipt")

3️⃣ Default Parameters

Parameter has a default value if no argument is passed.

def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Pradipt")

4️⃣ Variable-Length Parameters (*args)

Allows multiple positional arguments.

def total(*nums):
    print(sum(nums))

total(1, 2, 3, 4)

5️⃣ Keyword Variable-Length Parameters (**kwargs)

Allows multiple keyword arguments.

def details(**data):
    print(data)

details(name="Pradipt", age=21)
'''
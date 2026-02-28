# a=list(input('Enter a value : '))
# print(a+500)

#11
# n = int(input('Enter a value! '))

# if n>100:
#     print(True)
# else:
#     print(False)

# a = input('Enter a value! ')

# s = a[::-1]
# print(s)
# if s==a:
#     print(True)
# else:
#     print(False)  

# a = int(input('Enter a value! '))

# if a>40:
#     print("HOT")
# else:
#     print("Cold")  


# name= "PP"
# password = "idk"

# n = input('Enter a name: ')
# p = input('Enter a password: ')

# if n==name and password==p:
#     print(True)
# else:
#     print(False)


# a = int(input('Enter a value! '))
# b = int(input('Enter a value! '))

# print("sum ", a+b)
# print("sub ", abs(a-b))


# a = int(input('Enter a value! '))

# if a>10 and a<50:
#     print("in range")
# else:
#     print("not in range")  

# a = int(input('Enter a value! '))

# if a>=100 and a<1000:
#     print("Yes It is")
# else:
#     print("Not a 3-digit number")  

# a = input('Enter a value! ')

# if len(a)>5 :
#     print("Yes It is")
# else:
#     print("length less than 5")  

# a = int(input('Enter a value! '))

# if a==0:
#     print("Yes It is")
# else:
#     print("Not a zero value")  

# Id= "xyz"

# id = input('Enter a id: ')
# age = int(input('Enter a age: '))

# if id==Id and age>=18:
#     print("Yes, Go for it, You are Eligible")
# else:
#     print("Not Eligible!")


# age = int(input("Enter age"))
# income = int(input("Enter income"))
# credit = int(input("Enter credit"))


# if age>=21:
#     if income >=2500:
#         if credit >=700:
#             print("Loan Approved!")
#         else:
#             print("Loan Rejected (Low Credit Score)")
#     else:
#         print("Loan Rejected (Low income)")
# else:
#     print("Loan Rejected (Age not Eligible)")


# cpp = int(input("Enter cpp: "))
# python = int(input("Enter python: "))
# DSA = int(input("Enter DSA: "))

# if cpp>=40 and python>=40 and DSA>=40:
#     avg = (cpp+python+DSA)/3
#     if avg >=75:
#         print('Distinction!!!')
#     else:
#         print('Pass!!!')
# else:
#     print('Fail!')


# income = int(input("Enter income: "))

# if income>500000:
#     if income<1000000:
#         print("20% TAX")
#     else:
#         print("30% TAx")
# else:
#     if income>250000:
#         print("5% TAX")
#     else:
#         print("NO TAX")

# num = 50

# while num>=40:
#     print(num)
#     num-=1


# num = 0

# while num<10:
#     print(num*2)
#     num+=1

# num = int(input("Enter a number"))

# val =0
# while num != 0:
#     val = val*10 + num%10
#     num//=10
# print(val)

# ss = input("Enter a string value: ")

# i =len(ss)-1
# s = ""
# while i>=0:
#     s += ss[i]
#     i-=1
# print(s)

# num = 1
# val =0
# while num<10:
#     val += num*2
#     num += 1
# print(val)

# num = 3
# i =1
# while i<=10:
#     print(num, "*" , i, "=", num*i)
#     i+=1


# name = "Pradipt Prasoon"
# s=""
# for i in name:
#     if i == ' ':
#         s+="_"
#     else:
#         s+=i
# print(s)


# l = ["P1.py", "first.txt", "T2.py", "Tk.txt", "TFK.com"]

# d={}

# for i in l:
#     temp = i.split('.')
#     if temp[1] in d:
#         d[temp[1]].append( temp[0])
#     else:
#         d[temp[1]] = [temp[0]]
# print(d)

# l = "aaabbbxx"
# s=l[0]
# i = 0
# count = 1
# n = len(l)
# while i<n-1:
#     if l[i] == l[i+1]:
#         count+=1
#     else:
#         s += str(count)
#         s += l[i+1]
#         count=1
#     i+=1

# s+=str(count)
# print(s)

# l = [(2+4j), 12, "Program", "python", False]

# d ={}

# for i in l:
#     if type(i) == str:
#         t=''
#         for j in i:
#             if j in 'aeiouAEIOU':
#                 t+=j
#         d[i] = t
# print(d)

# dic = {"name": "Bhavik"}

# print(dic["name"][5:2:-1])

# for i in range(5):
#     for j in range(5):
#         print('*', end = " ")
#     print("\n")

# n = 10
# for i in range(1, n+1):
#     for j in range(i):
#         print('*', end=" ")
#     print()

# n = 10
# for i in range(1, n+1):
#     for j in range(n-i):
#         print('*', end=" ")
#     print()

# n = 3
# x=1
# for i in range(1, n+1):
#     j=0
#     while j<i:
#         j+=1
#         print(end=" ")
#     print('*')


# n = int(input("Enter row: "))
# m = int(input("Enter col: "))

# for i in range(1, n+1):
#     for j in range(1,  m+1):
#         print("#", end = " ")
#     print()

# n = int(input("Enter row: "))
# m = int(input("Enter col: "))

# for i in range(1, n+1):
#     for j in range(1,  m+1):
#         if i==j:
#             print("*", end= " ")
#         elif i<j:
#             print("@", end = " ")
#         else:
#             print("#", end=" ")
#     print()

# n = int(input("Enter row: "))
# m = int(input("Enter col: "))

# for i in range(1, n+1):
#     for j in range(1,  m+1):
#         if i+j == n+1:
#             print("*", end= " ")
#         else:
#             print(end="-")
#     print()

# n = int(input("Enter row: "))
# m = int(input("Enter col: "))

# for i in range(1, n+1):
#     for j in range(1,  m+1):
#         if i+j == n+1:
#             print("*", end= " ")
#         elif i+j < n+1:
#             print("@", end = " ")
#         else:
#             print("#", end=" ")
#     print()


n = int(input("Enter row: "))
m = int(input("Enter col: "))

for i in range(1, n+1):
    for j in range(1,  m+1):
        if i+j == n+1:
            print("#", end= " ")
        elif i==j and i+j <n+1:
            print("*", end = " ")
        elif i==j and i+j>=n+1:
            print("@", end=" ")
        else:
            print(end=" ")
    print()

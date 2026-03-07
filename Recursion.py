# n = int(input("Enter num = "))

# def fact1(n):
#     num =1
#     for i in range(1,n+1):
#         num*=i
#     print(num)
# fact1(n)


# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     return n*fact(n-1)

# print(fact(n))

def add(a, b, c, x=0, y=0):
    return a+b+c+x+y

print(add(2,4,5))
print(add(2,3,4,5))


def indSum(n):
    if n == 0:
        return 0
    return n%10 + indSum(n//10)
    

print(indSum(123))

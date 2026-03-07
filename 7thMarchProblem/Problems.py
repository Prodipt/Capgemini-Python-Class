# class Solution:
#     def strong_passwords(self, passwords):
#         strong = []

#         for pwd in passwords:
#             if (len(pwd) >= 8 and
#                 any(c.isupper() for c in pwd) and
#                 any(c.isdigit() for c in pwd) and
#                 any(c in "@#$" for c in pwd)):
#                 strong.append(pwd)
    
#         return strong


# class Solution:
#     def low_stock_products(self, inventory):
#         result = []
#         #Write your code here
#         for i in inventory:
#             if inventory[i] <10:
#                 result.append(i)
#         return result


# class Solution:
#     def find_duplicate_words(self, sentence):
#         words = sentence.lower().split()
#         duplicates = []
#         #Write your code here
#         for i in range(len(words)-1):
#             if words[i].lower() == words[i+1].lower():
#                 duplicates.append(words[i].lower())
#         return duplicates


# class Solution:
#     def unique_products(self, products):
#         result = []
#         #Write your code here
#         for i in products:
#             if products.count(i) == 1:
#                 result.append(i)
#         return result
# File Handling

# File is a type of container in which we contain or stor some data
# By using extension name, we can identify what type of data is store inside of it.
# Ex : .py, .mp4, .thml, .mp3, .png

# Before ahndling any file, taking permission is very much important

# open():
#      open()

# close():
#   var_name.close() 

# Total 3 different modes are oresent

# Write(w) , read(r), appwnd(A)

# write mode:
# only write(w),  write+read(w+), write binary(wb), write & read binary(wb+)

# A. write(string):

# read mode:
# only read(r),  read+write(r+), read binary(rb), read & write binary(rb+)


# append mode:
# only append(a),  append + read(ar), append  binary(ab), append & read binary(ab+)


# file = open("abc.txt", "r")

# file.write("HI I am writing this to you")

# file.writelines(["first_line\n", "2nd_line\n", "3rd_line\n"])

# print(file.readline())
# print(file.readline())
# print(file.readline())

# print(file.readlines())
# print(file.read())

# file.close()



file = open("temp1.txt", 'w+')

'Writing single line to the file'
# file.write("Hello world")

'Writing multiple lines to the file'
file.writelines([
    'first line\n'
    'second line\n'
    'third line\n'
    'fourth line\n'
    'fifth line\n'
    'sixth line'
])
file.seek(0) # go back to the initial position that is the first position
# (we are doing this for w+, as after writing it goes starts from the 
# current position and does not read what was executed earlier)

# file.write("hi")

'Reading the file'
# print(file.read())

# print(file.readline())
# print(file.readline())
# print(file.readline())

# print(file.readlines())

file.close()

import csv 
from datetime import date

file2 = open('expense.csv','a+')
w = csv.writer(file2)
w.writerow(['DATE', 'CATEGORY', 'AMOUNT']) # columns

w.writerows(
    [
    [date.today(), 'Travel', 200],
    [date.today(), 'Food', 200],
    [date.today(), 'Entertainment', 200]
    ]
)

file2.close()

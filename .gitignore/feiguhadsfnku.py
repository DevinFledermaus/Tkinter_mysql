# with open('Login_details.txt', 'rt') as myfile:  # Open lorem.txt for reading
#     for myline in myfile:              # For each line, read to a string,
#         print(myline)                  # and print the string.
#         # print(myline[-1])

with open('../Login_details.txt', 'r') as f:
    lines = f.read().splitlines()
    print(lines)

# import re
#
# fileToRead = 'user_details.txt'
# file = open(fileToRead, 'r')
# listLine = file.readlines()
# # print(listLine)
#
# text = str(listLine)
# print(text)
#
#
# emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
# print(emails)
#
# print(emails[-1])

# with open('user_details.txt', "r") as x:
#     lines = x.read().splitlines()
#     last_line = lines

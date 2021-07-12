# jabber = open("/Users/matrix/Desktop/2.1 sample.txt", "r")
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end ="")
#
# jabber.close()

# print("*"*40)

# In following program no need to close the file
# with open("/Users/matrix/Desktop/2.1 sample.txt", "r") as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end="")

# print("*"*40)


# with open("/Users/matrix/Desktop/2.1 sample.txt", "r") as jabber:
#     line = jabber.readline() #readline method read a line collectively while read method word by word
#     while line:
#         print(line, end="")
#         line = jabber.readline()

# print("*"*40)

# with open("/Users/matrix/Desktop/2.1 sample.txt", "r") as jabber:
#     lines = jabber.readlines()
#     print(lines, end='') #this is gonna return the list
#     for line in lines[::-1]:
#         print(line, end='')
# #
#
#
with open("/Users/matrix/Desktop/2.1 sample.txt", "r") as jabber:
    lines = jabber.read()
print(lines, end='')
print('*'*40)
for line in lines[::-1]:
    print(line, end='')
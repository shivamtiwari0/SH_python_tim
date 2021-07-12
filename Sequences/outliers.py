data = [4 ,5 , 104, 105, 110 , 120 , 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]
# del data[:2]
# print(data)
# del data[14:]
# print(data)
# program1
# min_valid = 100 #if you run this you'll find problem, debug it to know it
# max_valid = 200
# top_index = len(data)-1
# for index, value in enumerate(reversed(data)):
#     if value < min_valid or value > max_valid:
#         del data[top_index-index]
# print(data)


min_valid = 100  # if you run this you'll find problem, debug it to know it
max_valid = 200
# # program 2
# for index, value in enumerate(data):
#     if (value<min_valid) or (value>max_valid):
#         del data[index]
# print(data)

# program3
stop = None
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
print(stop)
del data[:stop]
print(data)  # output has removed values lower than 100
#
start = 0
for index in range(len(data)-1, -1, -1):
    if data[index] <= max_valid:
        start = index+1
        break
print(start)
del data[start:]
print(data)  # output has removed higher than 200
# mutable iterable loops are confusing

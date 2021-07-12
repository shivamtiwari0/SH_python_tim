data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]
min_valid = 100
max_valid = 200

# for index in range(len(data)-1, -1, -1):
#     if data[index]< min_valid or data[index]>max_valid:
#         del data[index]
#         print(index)
# print(data) #why this code works and code in ouliers.py doesn't, because it executing from backwards and index postion
# of next no to be executed doesn't changes.
top_index = len(data)-1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        del(data[top_index- index])
print(data)





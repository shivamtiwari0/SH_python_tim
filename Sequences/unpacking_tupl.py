x, y, z = 1, 2, 76
print(x)
print(y)
print(z)
print("Unpacking a tuple ")
data = x, y, z
print(x)
print(y)
print(z)

print("Unpacking a list ")  # list will crash while unpacking if we change them as they are mutable.
data_list = [12, 13, 14]
data_list.append(15)
p, q, r = data_list
print(p)
print(q)
print(r)


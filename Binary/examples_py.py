
# for i in range(17):
#     print("{0:>2} binary is {0:08b}".format(i))
#
#
# print("{0:0b}".format(65535))

## To convert value upto 65535 in binary
powers = []
for power in range(15, -1, -1):
    powers.append(2**power)
print(powers)

printing = False
a = int(input("Enter ur no. = "))
for value in powers:
    bit = a//value
    if bit != 0:
        printing = True
    if printing:
        print(bit, end='')
    a %= value

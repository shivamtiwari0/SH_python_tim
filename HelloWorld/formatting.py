for i in range(1, 13):
 print("{0:2} squared {1:<3}, cubed {2:>4}.".format(i, i**2, i**3))
 #{0:2} - 2 is field width for i output, {1:3}- 3 is field width for i**2.

print()
# print("Pi is {0:10.18f}.".format(22/7)) #10 is field width & 18 is decimal precision.
print("Pi is {0:20.18f}.".format(22/7)) #10 is field width & 18 is decimal precision.

print(f"Pi is {22/7:10.18f}.")




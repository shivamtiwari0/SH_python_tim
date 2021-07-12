even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
even.extend(odd)  # we pass the list odd to extend method to extend even.
# print(even)
# #
# a = sorted(even)
# print(a)
# print(even)
# even.sort() #sorted but in reverse order.
# print(even) #sort method is used to sort the even.
# # difference b/w sort and sorted in list- sorted method doesn't changed list even but sort method changed
# #list even
# even.reverse()
# print(even)
numbers = even + odd
# print(numbers)
#
more_numbers = numbers.copy()
print(more_numbers is numbers)
print(more_numbers == numbers)
# print(more_numbers)
#
# digits = list("12345")
# print(digits)
# xyz = sorted("45365248")
# print(xyz)


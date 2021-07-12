word1 = "abcd"  # strings are immutable
word2 = word1

print(id(word2))
print(id(word1))

word1 = "efgh"
print(id(word1))
print(id(word2))
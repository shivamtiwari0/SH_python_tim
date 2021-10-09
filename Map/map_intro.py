import timeit

text = "what have the romans ever done for us"


def capitals():
    capital = [char.upper() for char in text]
    return capitals


def map_capitals():  # map
    return map(str.upper, text)


def words():
    return [word.upper() for word in text.split(' ')]


def map_words():
    return list(map(str.upper, text.split(' ')))


# when we call a function as argument, don't use parenthesis. When we use parenthesis we are passing the result of
# function

# for x in map(str.upper, text.split(' ')):
#     print(x)

if __name__ == "__main__":
    print(timeit.timeit("capitals()", setup="from __main__ import capitals", number=10000))
    # print(timeit.timeit("map_capitals()", setup="from __main__ import map_capitals", number=10000))
    # print(timeit.timeit("words()", setup="from __main__ import words", number=10000))
    # print(timeit.timeit("map_words()", setup="from __main__ import map_words", number=10000))
    print(timeit.timeit(capitals, number=10000))
    print(timeit.timeit(map_capitals, number=10000))
    print(timeit.timeit(words, number=10000))
    print(timeit.timeit(map_words, number=10000))

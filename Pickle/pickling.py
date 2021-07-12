import pickle

# Imelda = ('More Mayhem',
#           'Imelda May',
#           '2011',
#           ((1, 'Pulling the Rug'),
#            (2, 'Psycho'),
#            (3, 'Mayhem'),
#            (4, 'Kentish Town Waltz')))
# with open('Imelda.pickle', 'wb') as pickle_file:
#     pickle.dump(Imelda, pickle_file)

# with open('Imelda.pickle', 'rb') as imelda_pickled:
#     imelda2 = pickle.load(imelda_pickled)
# print(imelda2)

##Program 2

# Imelda = ('More Mayhem',
#           'Imelda May',
#           '2011',
#           ((1, 'Pulling the Rug'),
#            (2, 'Psycho'),
#            (3, 'Mayhem'),
#            (4, 'Kentish Town Waltz')))
# even = list(range(2,10,2))
# odd = list(range(1, 10, 2))
#
# with open('Imelda.pickle', 'wb') as pickle_file:
#     pickle.dump(Imelda, pickle_file)
#     pickle.dump(even, pickle_file)
#     pickle.dump(odd, pickle_file)
#     pickle.dump(2998302, pickle_file)
#
with open('Imelda.pickle', 'rb') as imelda_pickled:  # Object must be written in the same order as they written above
    imelda = pickle.load(imelda_pickled)
    print(imelda)
    even_list = pickle.load(imelda_pickled)
    print(even_list)
    odd_list = pickle.load(imelda_pickled)
    print(odd_list)
    x = pickle.load(imelda_pickled)
    print(x)


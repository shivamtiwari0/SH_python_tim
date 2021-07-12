with open("2.1 sample.txt", 'w') as sample_table:
    for i in range(1, 13):
        print("{:2} times 2 is {:1}".format(i, i*2), file=sample_table)

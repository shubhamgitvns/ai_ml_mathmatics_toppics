# Mean - Mean is the average of a set of numbers.

def mean(number):
    n = len(number)
    total = 0
    for i in number:
        total += i
    mean = total/n
    return mean
print("Mean =",mean([10, 20, 14, 15, 23, 40, 9, 29]))

# Median - The middle value in a sorted set of numbers

def median(number):

    number.sort()

    n = len(number)

    middle = n // 2

    if n % 2 == 0:

        median = (number[middle - 1] + number[middle]) / 2

    else:

        median = number[middle]

    return median
print("Median =",median([10, 20, 14, 15, 23, 40, 9, 29]))

# Mode - The most frequent value in a set 

def mode(number):

    d = {}

    for i in number:

        d[i] = number.count(i)

    for mode, value in d.items():

        if value == max(d.values()):

            return mode


print("Mode =",mode([1,2,2,2,3,3,3,4,5]))




# Median - The middle value in a sorted set of numbers

number= [10, 20, 14, 15, 23, 40, 9, 29]
number.sort()
n = len(number)
middle = n//2
print(number)

if n % 2 == 0:
    midian = (number[middle - 1] + number[middle])/2
   
else:
    midian = number[middle]
print(midian)
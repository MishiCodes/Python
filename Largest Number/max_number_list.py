#largest no in list
numbers = [3,6,4,8,2,10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
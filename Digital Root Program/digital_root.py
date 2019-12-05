def digital_root(n):

    while n >= 10:
        n = sum([int(x) for x in str(n)]) #list comprehension
    return n

print(digital_root(16))

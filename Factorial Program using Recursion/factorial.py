def factorial(number):
    
    if number == 0: # 0! is 1
        return 1
    else:
        return number*factorial(number-1)  # using recursion

print(factorial(3))

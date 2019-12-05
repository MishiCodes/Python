numbers = [1, 2, 3, 4, 5]

# --------- Method 1: Using list comprehension-------------
my_list = [n*2 for n in numbers]  
print(my_list)

# ---------- Method 2: Using map()--------------------------
def multiply_by_two(number):
    return number * 2

my_list = map(multiply_by_two, numbers)
print(list(my_list)) # convert the map object into a list, for readability

# ---------- Method 3: Using a map + lambda------------------
my_list = map(lambda n: n*2, numbers)
print(list(my_list))

# ---------- Method 4: Using list append with for loop--------
my_list = []
for n in numbers:
    my_list.append(n*2)
print(my_list)

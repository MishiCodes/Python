### An ICA supermarket attendant works every day selling to customers. They have a business where each item you buy, mjolk, 
Pannkakor, Bröd, Paj, and everything there costs a positive number of Kroner (integers). If bröd costs 22 kroner. There is no 
item in ICA that costs a decimal value like 10.13 kr (VAT tax is included in the amount already).
Kroner change can be provide in 1 kr, 2kr, 5kr and 10kr.
Write a function in Python that takes in two arguments will return the correct change to the customer with the smallest possible
number of coins (or bills if paper money is used).

#### [HOW TO RUN YOUR PYTHON SCRIPTS FROM COMMAND LINE?](https://docs.python.org/3/faq/windows.html)
* Search for command prompt or type in cmd to do so
* Switch to the python file directory OR path to your script
* In command-line, type in the word python or python3 if you have both versions and the name of python file just like this: $ python3 multiply_by_two.py

![Run Python Script](https://github.com/MishiCodes/Python/blob/master/1.%20Python%20Lists/Images/Screenshot%20from%202019-12-05%2004-57-09.png)

#### __Explanation of methods used for solution__

#### [PYTHON LIST COMPREHENSION](https://www.pythonforbeginners.com/basics/list-comprehensions-in-python)
> _List comprehensions provide a concise way to create lists_
> _It consists of brackets containing an expression followed by a for clause, thenzero or more for or if clauses. The expressions >can be anything, meaning you can put in all kinds of objects in lists_
> * Syntax: [expression for item in list]

#### [PYTHON map() FUNCTION](https://www.w3schools.com/python/ref_func_map.asp)
> _The map() function executes a specified function for each item in a iterable. The item is sent to the function as a parameter_
> * Syntax: map(function, iterables)

#### [PYTHON lambda-aNONYMOUS FUNCTIONS](https://medium.com/better-programming/lambda-map-and-filter-in-python-4935f248593)
> _A lambda operator or Lambda function is used for creating small, one-time, anonymous function onjects in Python_
> _A lambda operator can have any number of arguments but can have only one expression_
> * Syntax: lambda arguments : expression

#### [PYTHON LIST APPEND]()
>_The append() method adds a single item to the end of the list_
> * Syntax: list.append(item)
> * item - an item to be added at the end of the list

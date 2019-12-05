### A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value 
### has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.

##### Here's how it works:

digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6

#### [HOW TO RUN YOUR PYTHON SCRIPTS FROM COMMAND LINE?](https://docs.python.org/3/faq/windows.html)
* Search for command prompt or type in cmd to do so
* Switch to the python file directory OR path to your script
* In command-line, type in the word python or python3 if you have both versions and the name of python file just like this: $ python3 digital_root.py

#### __Explanation of methods used for solution__

#### [PYTHON LIST COMPREHENSION](https://www.pythonforbeginners.com/basics/list-comprehensions-in-python)
> _List comprehensions provide a concise way to create lists_
> _It consists of brackets containing an expression followed by a for clause, thenzero or more for or if clauses. The expressions >can be anything, meaning you can put in all kinds of objects in lists_
> * Syntax: [expression for item in list]

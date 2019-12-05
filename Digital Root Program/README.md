### A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value 
has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.

##### Here's how it works:

digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6

#### __Explanation of methods used for solution__

#### [PYTHON LIST COMPREHENSION](https://www.pythonforbeginners.com/basics/list-comprehensions-in-python)
> _List comprehensions provide a concise way to create lists_
> _It consists of brackets containing an expression followed by a for clause, thenzero or more for or if clauses. The expressions >can be anything, meaning you can put in all kinds of objects in lists_
> * Syntax: [expression for item in list]

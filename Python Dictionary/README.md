
### Design a phone book program. In this program, we can think of a phone book as a collection of friends, associates, family with their information such as a telephone number, email address, name and location. Design a simple program that gets the names from a random list like:
_names = [‘Jasmine’, ‘Alexandra’, ‘Bojana’]_
_location = [‘stockholm’, ‘goteborg’, ‘helsingborg’]_

_def phoneBook(names, location):_
    _return dict(zip(names, location))_

### Please design an algorithm, not the fancy code you see in the illustration above, that will create key value pairs of name and location at the end, use constructs like for-loops.
### Extra credit: You can make your application return data or output that looks fancier (this looks like JSON):
_{
‘Jasmine’: { ‘location’: ‘stockholm’},
‘Alexandra’: { ‘location’: ‘goteborg’},
‘Bojana’: { ‘location’: ‘helsingborg’},
}_
#### [HOW TO RUN YOUR PYTHON SCRIPTS FROM COMMAND LINE?](https://docs.python.org/3/faq/windows.html)
* Search for command prompt or type in cmd to do so
* Switch to the python file directory OR path to your script
* In command-line, type in the word python or python3 if you have both versions and the name of python file just like this: $ python3 phone_book.py

![Run Python Script](https://github.com/MishiCodes/Python/blob/master/Python%20Dictionary/Screenshot%20from%202019-12-05%2016-30-59.png)

#### [PYTHON DICTIONARY COMPREHENSION](https://cmdlinetips.com/2018/01/5-examples-using-dict-comprehension/)
> _In Python, dictionary is a data structure to store data such that each element of the stored data is associated with a key. Dictionary data structure lets you query the data using key very efficiently._
> * Syntax: {key:value for i in list}

# Python
The basic concepts and features of the Python language

### Introduction
Python is a general purpose high level programming language. Created by **Guido van Rossum** in 1989 at NRI, Netherland, But officially available to the public 1991(20-Feb-1991) and was named after the BBC TV show Monty Python’s Flying Circus.

Example:
``` 
>>> print("Hello world!")
Hello world!
>>> a, b = 10, 20
>>> print(a + b)
30
>>> a, b, c, d, e = 10, 20, 30, 40, 50
```
 C, Java are statically typed programming languages, but python is dynamically typed programming language.
 
 Example:
```
>>> a = 10
>>> type(a)
<class 'int'>
>>> b = True
>>> type(b)
<class 'bool'>
```

### Features borrowed from:
- Functional programming from C
- OOP from C++
- Scripting language features from Perl and Shell script
- Modular programming features from Module-3
- Most of the Syntaxes are from C and ABC languages

### Applications
- Desktop applications
- Web applications
- Database applications
- For Network applications
- Games
- Data analysis
- Machine learning
- AI
- IOT applications
### Features of Python
- Simple & easy to learn
- There are total 33 reserved keywords are there
- Freeware and open source
- High level programming language (i.e human understandable language)
- Python is platform independent (i.e write once and run any where (WORA))
- Portability (i.e you can migrate your python program to other operating system without changing anything)
- Dynamically typed programming language
- Procedure oriented and Object oriented programming language
- Interpreted language (i.e Python interpreter will take care the compilation)
- Extensible (i.e Third party tools like Cython, cffi, SWIG and Numba offer both simpler and more sophisticated approaches to creating C and C++ extensions for Python)
- Embedded (i.e Embedding is inserting calls into your C or C++ application after it has started up in order to initialize the Python interpreter and call back to Python code at specific times)
- Extensive library

### Identifiers
A name in python program is called "Identifier". It may be variable name or class name or method name.

#### Rules to define identifiers in python
- alphabet (both upper case and lower case)
- digits (0 - 9), but should not start with digit
- Underscore ( _ )
- Python identifiers are case sensitive
- Reserved keywords are not allowed to use as identifiers
- There is no length for identifier names, but it is not recommended to take too lengthy identifiers
- Underscore( _ ), if identifier starts with underscore( _ ) symbol then it indicates that private
- Double underscore ( _ _ ), if identifiers starts with double underscore symbols then it indicates that strong private
- \_\_str\_\_ , \_\_main\_\_, if identifier starts with 2 underscore symbols and ends with 2 underscore symbols, then it is language specific identifier. It is special variable defined by python itself. We can use these in overloaded operators

### Reserved keywords
- True, False, None
- if, else, elif
- and, or, not, is
- while, for, break, continue, in, return, yield
- try, except, finally, raise, assert
- import, from, as, class, def, pass, global, nonlocal, lambda, del, with

Note:
- All reserved words contains only alphabets
- Except True, False and None remaining all reserved words starts with only small  case alphabets

Example:
```
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

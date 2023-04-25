Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> rows = 5
... b = 0
... # reverse for loop from 5 to 0
... for i in range(rows, 0, -1):
...     b += 1
...     for j in range(1, i + 1):
...         print(b, end=' ')
...     print('\r')
...     
SyntaxError: multiple statements found while compiling a single statement
>>> print("hello world")
hello world
>>> print ("khan saheb");
khan saheb

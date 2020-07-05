Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a, *y = {1:2, 3:4, 5:6}
>>> a
1
>>> y
[3, 5]
>>> a
1
>>> *y
SyntaxError: can't use starred expression here
>>> y
[3, 5]
>>> a
1
>>> 

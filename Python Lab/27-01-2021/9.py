Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:10:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def change_sring(str1):
      return str1[-1:] + str1[1:-1] + str1[:1]

>>> print(change_sring('banana'))
aananb
>>> 
Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:10:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def Merge(dict1, dict2):
    return(dict2.update(dict1))

>>> dict1 = {'a': 10, 'b': 8}
>>> dict2 = {'d': 6, 'c': 4}
>>> print(Merge(dict1, dict2))
None
>>> print(dict2)
{'d': 6, 'c': 4, 'a': 10, 'b': 8}
>>> 
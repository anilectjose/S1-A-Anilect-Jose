Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:10:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import operator
>>> d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
>>> print('Original dictionary : ',d)
Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
>>> sorted_d = sorted(d.items(), key=operator.itemgetter(1))
>>> print('Dictionary in ascending order by value : ',sorted_d)
Dictionary in ascending order by value :  [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
>>> sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
>>> print('Dictionary in descending order by value : ',sorted_d)
Dictionary in descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}
>>> 
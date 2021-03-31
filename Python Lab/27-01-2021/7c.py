Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:10:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1 = [10, 10, 11, 12, 12, 13, 14, 16, 15, 16, 12]
>>> list2 = [10, 10, 11, 12, 12, 16, 14, 16, 15, 19, 12]
>>> for value in list1:
      if value in list2:
         common=1

>>> if common==1:
	print("there are common elements")
else:
	print("no common elements")

there are common elements
>>> 
Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:10:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> list = [11, 22, 33, 44, 55]
>>> print(list)
[11, 22, 33, 44, 55]
>>> for i  in list:
	if(i%2 == 0):
		list.remove(i)

		
>>> print("list after removing EVEN numbers:")
list after removing EVEN numbers:
>>> print(list)
[11, 33, 55]
>>> 
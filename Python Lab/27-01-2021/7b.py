Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:10:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1 = [10, 10, 11, 12, 12, 13, 14, 16, 15, 16, 12]
>>> list2 = [16, 12, 13, 14, 15, 16, 10, 11, 12, 10, 12]
>>> total1= sum(list1)
>>> total2=sum(list2)
>>> if total1 == total2 :
	print('both list have equal sum')
else:
	print('both list doesnt have equal sum')


both list have equal sum
>>> 
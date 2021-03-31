Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:10:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print ("Enter year")
Enter year
>>> endYear = int(input())
2030
>>> startYear =2020
>>> print ("List of leap years:")
List of leap years:
>>> for year in range(startYear, endYear):
	if (0 == year % 4) and (0 != year % 100) or (0 == year % 400):
		 print (year)

		 
2020
2024
2028
>>> 
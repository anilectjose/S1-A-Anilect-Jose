Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:10:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> stringA = "Hii how are you"
>>> print("Given String: \n",stringA)
Given String: 
 Hii how are you
>>> vowels = "AaEeIiOoUu"
>>> res = set([each for each in stringA if each in vowels])
>>> print("The vlowels present in the string:\n ",res)
The vlowels present in the string:
  {'o', 'i', 'u', 'a', 'e'}
>>> 
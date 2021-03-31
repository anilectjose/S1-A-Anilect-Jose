Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:10:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def gcd(a,b):
     
    # Everything divides 0 
    if (b == 0):
         return a
    return gcd(b, a%b)

>>> a = 98
>>> b = 56
>>> if(gcd(a, b)):
    print('GCD of', a, 'and', b, 'is', gcd(a, b))
else:
    print('not found')

    
GCD of 98 and 56 is 14
>>> 
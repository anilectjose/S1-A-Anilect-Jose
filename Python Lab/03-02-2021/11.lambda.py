print('Enter the length of a side of square')
s = int(input("Enter your value: "))
print('Enter the length and breadth of rectangle')
l = int(input("Enter your value: "))
b = int(input("Enter your value: "))
print('Enter the base and height of triangle')
h = int(input("Enter your value: "))
d = int(input("Enter your value: "))
x = lambda s: s * s
y = lambda l, b: l * b
t = 0.5
z = lambda h, d, t: h * d * t
print("Area of square is :", x(s))
print('Area  of rectangle', y(l, b))
print('Area of triangle', z(h, d, t))

# Enter the length of a side of square
# Enter your value: 2
# Enter the length and breadth of rectangle
# Enter your value: 4
# Enter your value: 6
# Enter the base and height of triangle
# Enter your value: 5
# Enter your value: 6
# Area of square is : 4
# Area  of rectangle 24
# Area of triangle 15.0

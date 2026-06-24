# Day 3: 30 Days of python programming
# File: 30DaysOfPython/day_3/operators.py
# Exercises: Operators

import math

# ─────────────────────────────────────────────
# Q1. Age as integer
age = 20
print("Age:", age, "| Type:", type(age))

# Q2. Height as float
height = 5.9
print("Height:", height, "| Type:", type(height))

# Q3. Complex number variable
complex_num = 3 + 4j
print("Complex Number:", complex_num, "| Type:", type(complex_num))

# ─────────────────────────────────────────────
# Q4. Area of a triangle (area = 0.5 x b x h)
base   = float(input("Enter base: "))
height = float(input("Enter height: "))
area_of_triangle = 0.5 * base * height
print("The area of the triangle is", area_of_triangle)

# ─────────────────────────────────────────────
# Q5. Perimeter of a triangle (perimeter = a + b + c)
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a + b + c
print("The perimeter of the triangle is", perimeter)

# ─────────────────────────────────────────────
# Q6. Rectangle — area and perimeter
length = float(input("Enter length of rectangle: "))
width  = float(input("Enter width of rectangle: "))
rect_area      = length * width
rect_perimeter = 2 * (length + width)
print("Area of rectangle:", rect_area)
print("Perimeter of rectangle:", rect_perimeter)

# ─────────────────────────────────────────────
# Q7. Circle — area and circumference (pi = 3.14)
pi     = 3.14
radius = float(input("Enter radius of circle: "))
circle_area  = pi * radius * radius
circumference = 2 * pi * radius
print("Area of circle:", circle_area)
print("Circumference of circle:", circumference)

# ─────────────────────────────────────────────
# Q8. Slope, x-intercept and y-intercept of y = 2x - 2
# y = mx + c  →  y = 2x - 2  →  m=2, c=-2
# x-intercept: set y=0  →  0 = 2x - 2  →  x = 1
# y-intercept: set x=0  →  y = -2
slope       = 2
x_intercept = 1
y_intercept = -2
print("Slope:", slope)
print("X-intercept:", x_intercept)
print("Y-intercept:", y_intercept)

# ─────────────────────────────────────────────
# Q9. Slope and Euclidean distance between (2,2) and (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_q9    = (y2 - y1) / (x2 - x1)
distance    = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Slope between (2,2) and (6,10):", slope_q9)
print("Euclidean Distance:", distance)

# ─────────────────────────────────────────────
# Q10. Compare slopes from Q8 and Q9
print("Are slopes equal?", slope == slope_q9)   # True (both are 2)

# ─────────────────────────────────────────────
# Q11. y = x^2 + 6x + 9  →  find x where y = 0
# Factored: (x + 3)^2 = 0  →  x = -3
x = -3
y = x**2 + 6*x + 9
print("y at x =", x, "→", y)   # y = 0 when x = -3

# ─────────────────────────────────────────────
# Q12. Length of 'python' and 'dragon' — falsy comparison
len_python = len('python')   # 6
len_dragon = len('dragon')   # 6
print("Length of python:", len_python)
print("Length of dragon:", len_dragon)
print("Is len('python') != len('dragon'):", len_python != len_dragon)   # False (falsy)

# ─────────────────────────────────────────────
# Q13. Check if 'on' is in both 'python' and 'dragon' using 'and'
print("'on' in 'python' and 'dragon':", ('on' in 'python') and ('on' in 'dragon'))   # True

# ─────────────────────────────────────────────
# Q14. Check if 'jargon' is in the sentence using 'in'
sentence = "I hope this course is not full of jargon"
print("Is 'jargon' in sentence:", 'jargon' in sentence)   # True

# ─────────────────────────────────────────────
# Q15. There is no 'on' in BOTH dragon and python — False, 'on' exists in both
print("'on' not in 'dragon' and 'on' not in 'python':",
      ('on' not in 'dragon') and ('on' not in 'python'))  # False

# ─────────────────────────────────────────────
# Q16. Length of 'python' → float → string
length_python     = len('python')            # int: 6
length_as_float   = float(length_python)     # float: 6.0
length_as_string  = str(length_as_float)     # str: '6.0'
print("int:", length_python, "| float:", length_as_float, "| str:", length_as_string)

# ─────────────────────────────────────────────
# Q17. Check if a number is even (remainder == 0 when divided by 2)
num = 8
print("Is", num, "even?", num % 2 == 0)    # True

# ─────────────────────────────────────────────
# Q18. Check if floor division of 7 by 3 equals int(2.7)
print("7 // 3 == int(2.7):", 7 // 3 == int(2.7))   # True (both are 2)

# ─────────────────────────────────────────────
# Q19. Check if type of '10' equals type of 10
print("type('10') == type(10):", type('10') == type(10))   # False (str vs int)

# ─────────────────────────────────────────────
# Q20. Check if int('9.8') equals 10
# int() cannot directly convert a float string — must convert via float first
print("int(float('9.8')) == 10:", int(float('9.8')) == 10)  # False (int of 9.8 is 9)

# ─────────────────────────────────────────────
# Q21. Weekly earnings calculator
hours        = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
weekly_earning = hours * rate_per_hour
print("Your weekly earning is", weekly_earning)

# ─────────────────────────────────────────────
# Q22. Seconds a person has lived
years   = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print("You have lived for", seconds, "seconds.")

# ─────────────────────────────────────────────
# Q23. Display the table: n | 1 | n | n^2 | n^3
for n in range(1, 6):
    print(n, 1, n, n**2, n**3)

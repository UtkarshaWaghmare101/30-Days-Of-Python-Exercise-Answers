# Day 2: 30 Days of python programming
# File: 30DaysOfPython/day_2/variables.py
# Level 1 Exercises

# ─────────────────────────────────────────────
# Q1 & Q2 — The folder 30DaysOfPython/day_2/ and file variables.py are created. The comment # Day 2: 30 Days of python programming is at the top.

# Q3. First name variable
first_name = "gojo"

# Q4. Last name variable
last_name = "satoru"

# Q5. Full name variable
full_name = " gojo satoru"

# Q6. Country variable
country = "japan"

# Q7. City variable
city = "shibuya"

# Q8. Age variable
age = 26

# Q9. Year variable
year = 2026

# Q10. Marital status variable
is_married = False

# Q11. Boolean true variable
is_true = True

# Q12. Light switch variable
is_light_on = True

# Q13. Multiple variables on one line
name, gender, hobby = "gojo", "Male", "Coding"


# ─────────────────────────────────────────────
# LEVEL 2 EXERCISES
# ─────────────────────────────────────────────

# Q1. Check data type of all variables using type()
print(type(first_name))     # <class 'str'>
print(type(last_name))      # <class 'str'>
print(type(full_name))      # <class 'str'>
print(type(country))        # <class 'str'>
print(type(city))           # <class 'str'>
print(type(age))            # <class 'int'>
print(type(year))           # <class 'int'>
print(type(is_married))     # <class 'bool'>
print(type(is_true))        # <class 'bool'>
print(type(is_light_on))    # <class 'bool'>

# Q2. Find the length of first name
print(len(first_name))      # 8

# Q3. Compare length of first name and last name
print(len(first_name) > len(last_name))     # True / False
print(len(first_name) == len(last_name))    # True / False

# ─────────────────────────────────────────────
# Q4. Declare num_one and num_two
num_one = 5
num_two = 4

# Q5. Addition
total = num_one + num_two
print("Total:", total)              # 9

# Q6. Subtraction
diff = num_one - num_two
print("Difference:", diff)          # 1

# Q7. Multiplication
product = num_one * num_two
print("Product:", product)          # 20

# Q8. Division
division = num_one / num_two
print("Division:", division)        # 1.25

# Q9. Modulus (remainder)
remainder = num_two % num_one
print("Remainder:", remainder)      # 4

# Q10. Exponentiation (power)
exp = num_one ** num_two
print("Exponent:", exp)             # 625

# Q11. Floor division
floor_division = num_one // num_two
print("Floor Division:", floor_division)    # 1

# ─────────────────────────────────────────────
# Q12. Circle calculations (radius = 30 meters)
import math

radius = 30

# Q12a. Area of circle
area_of_circle = math.pi * radius ** 2
print("Area of Circle:", area_of_circle)

# Q12b. Circumference of circle
circum_of_circle = 2 * math.pi * radius
print("Circumference of Circle:", circum_of_circle)

# Q12c. Take radius as user input and calculate area
user_radius = float(input("Enter radius: "))
user_area = math.pi * user_radius ** 2
print("Area of Circle (user input):", user_area)

# ─────────────────────────────────────────────
# Q13. Get user input for personal details
first_name = input("Enter your first name: ")
last_name  = input("Enter your last name: ")
country    = input("Enter your country: ")
age        = int(input("Enter your age: "))

print(first_name, last_name, country, age)

# ─────────────────────────────────────────────
# Q14. Check Python reserved keywords
help('keywords')

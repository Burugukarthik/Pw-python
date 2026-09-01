# name="John"
# age=30
# sal=50000.50

name,age,sal="John",30,5000.50

# Approach1
print(name,age,sal)

# Approach 2
# Name is: John
# Age is: 30
# Salary is: 5000.50

print("Name is :"+name)
# print("Age is"+age)  # we cannot use concatenation between String and Num
print ("Age is",age)
print("Salary is" ,sal)
# Approach 3
print(f"Name is {name} and age is {age}")

'''
For modern Python, the best approach is f-strings.

Ranking of Approaches
1. ✅ f-strings (Recommended)
name = "John"
age = 30
salary = 5000.50

print(f"Name: {name}, Age: {age}, Salary: {salary}")

Advantages:

Easy to read
Fast
No need for type conversion (str(age))
Most commonly used in real projects
'''

# Output formatting means displaying data in a neat and controlled way.

x=input("Enter your name:")
y=input("Enter your age:")

print(f"Your name is {x} and your age is {y}")
"""
In Playwright with Python, f-strings are very useful for:

1. Dynamic URLs ---
username = "admin"

page.goto(f"https://example.com/users/{username}")

2. Dynamic Locators
product_name = "iPhone"

page.locator(f"text={product_name}").click()

f"..." is called an f-string or formatted string literal in Python.
 It is used for string interpolation, where variables or expressions are embedded directly inside a
  string using {}. 
In Playwright, f-strings are commonly used for dynamic URLs, locators, test data, logging messages, 
  file names, and screenshot paths.
"""

# Approach 4
c="KArthik"
d=24
print("Name :{} Age :{} ".format(c,d))

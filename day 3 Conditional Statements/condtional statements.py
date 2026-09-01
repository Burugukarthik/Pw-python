'''
"What are conditional statements in Python?"

Good Answer:

Conditional statements in Python are used to make decisions in a program based on whether a condition
is True or False. They control the flow of execution and allow different blocks of code to run depending
 on the result of a condition.

Python provides if, if-else, and if-elif-else statements for decision-making.

# if esle
age=23
if age>=18:
    print("Candidate is Eligible to caste vote")  #indentation is requried means space is required
else :
    print("Candidate is not Eligible to caste is vote")
'''
"""
# Check the amount value after discount
amount=12000
discount=0
if amount>10000:
    discount=amount*10/100
    final_amount=amount - discount
    print(f"Actual amount  {amount}")
    print(f"Discount amount after discount {discount}")
    print(f"Final amount after discount {final_amount}")

marks=70
if marks>=90:
    print("A+ Grade")
elif marks>=80:
    print("A Grade")
else :
    print ("B Grade")
    
    More than two conditions we use if elif else
"""
amount=15000

if amount >= 10000:
    discount=amount*20/100
    final_amount=amount - discount
    print(f"After Discount  {final_amount}")
elif amount >50000:
    discount=amount*10/100
    final_amount=amount - discount
    print(f"After Discount  {final_amount}")
elif amount >3000:
    discount=amount*15/100
    final_amount=amount - discount
    print(f"After Discount  {final_amount}")
else:
    discount=0
    print (f"No Discount Applicable {amount}")
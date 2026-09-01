#The Match statement is used to perform differnt actions based on different conditions.
#Instead of writing many if...else statements, you can use the match statement.
#day=int(input("Enter day number (1-7):" ))

"""
match day:
    case 1: print("sunday")
    case 2: print("monday")
    case 3: print("tuesday")
    case 4: print("wednesday")
    case 5: print("thursday")
    case 6: print("friday")
    case 7: print("saturday")
    case _: print("invalid day")
    """


'''
browser=input("enter your browser")

match browser:
    case "chrome": print("chrome")
    case "firefox": print("firefox")
    case "safari": print("safari")
    case _: print("invalid Browser")
'''
# example 2: combine values
""" 
Use the pipe charecter "|" as an operator  in the case evalution to check for 
more than one value in one case
pipe is represting "OR"

"""
"""
day=4
day=int(input("enter your day"))
match day:
    case 2| 3| 4| 5| 6: print("Weekday")
    case 1| 7: print("weekend")
    case _: print("invalid week")
"""
day=str(input("enter your day"))
match day:
    case "Sunday": print("1")
    case 'Monday': print("2")
    case 'Tuesday': print("3")
    case 'Wednesday': print("4")
    case 'Thursday': print("5")
    case 'Friday': print("6")
    case 'Saturday': print("7")
    case _: print("invalid day")

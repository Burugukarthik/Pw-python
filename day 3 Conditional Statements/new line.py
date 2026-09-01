print("welcome to \n python")
print("welcome to\t python")

'''
\n is called the newline escape character in Python.

It is used to move the cursor to the next line while printing text.


Uses in Python Automation (Selenium/Playwright)
--------------------------------------------------

1. Creating Readable Logs

username = "admin"

print(f"Starting Test\nUsername: {username}\nLogin Successful")

Output:

Starting Test
Username: admin
Login Successful


2. Writing Reports or Log Files

with open("testlog.txt", "a") as file:
    file.write("Test Started\n")
    file.write("Login Passed\n")
    file.write("Test Completed\n")

Output in file:

Test Started
Login Passed
Test Completed

\n is a newline escape character in Python. It is used to move the cursor to the next line within a string. 
In automation frameworks such as Selenium or Playwright, it is commonly used for formatting logs, 
reports, test results, email content, and file output to improve readability.
'''
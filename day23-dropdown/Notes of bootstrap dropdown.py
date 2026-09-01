'''
How to Remember When to Write Loops & Conditions
Instead of memorizing lines of code, remember the Three Golden Questions of automation:

'''
'''
1. "Am I dealing with a list of multiple elements?"
If the answer is Yes, you almost always need a for loop.

Whenever you use a locator that matches multiple items (like all span tags inside a dropdown menu), 
Python treats it as a collection. To look at them individually, you must loop through them using their index (nth(i)).

2. "Do I just want to look at everything, or do I want to find something specific?"
If you just want to look/print everything: You write a plain for loop with a print statement inside. 
No if condition is needed because you want the action to happen to every single item. (This was your first loop).

If you are searching for a specific target: You need an if condition inside the loop to act as a filter.

'''
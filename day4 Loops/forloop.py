"""
for understanding for loop we have first understandd "range()" function.
range() - function ... It will generate a sequence of numbers.
syntax-- range(start, stop, step)  start means where we need to start ,stop where we need to stop , step means inc or dec
range(num) #if you give single number that will be considered as stopping point
  in this case 0 is starting point
"""
'''
range()is a built-in Python function that generates a sequence of numbers and is commonly used with loops for iteration. 
The stop value is always excluded.

range(start, stop, step)
Start = where to begin
Stop = where to end (NOT included)
Step = how much to jump
range(5)        → 0 1 2 3 4
range(2,5)      → 2 3 4
range(1,10,2)   → 1 3 5 7 9
range(10,0,-1)  → 10 9 8 7 6 5 4 3 2 1

"Where have you used loops in automation?"

You can say:

"I use loops to iterate through web table rows, process multiple test data records, execute repeated actions, 
implement retry mechanisms, validate lists of elements, and run tests multiple times."
'''
'''
# Example 1:Only stopping value
print(list(range(10)))
print(list(range(0,10)))
'''
'''
for loop syntax
for variable in sequence:
    statement
'''
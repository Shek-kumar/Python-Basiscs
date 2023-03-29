# Arbitrary arguments allow us to pass a varying number of values during a function call.
# We use an asterisk (*) before the parameter name to denote this kind of argument.

# program to find sum of multiple numbers 

def find_sum(*numbers):
    result = 0
    
    for num in numbers:
        result = result + num
    
    print("Sum = ", result)

# function call with 3 arguments
find_sum(1, 2, 3)

# function call with 2 arguments
find_sum(4, 9)
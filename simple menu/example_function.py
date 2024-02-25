# example of function 
def my_function():
    print("Hello from a function", end = '')
    print("hello")
my_function()

def read_string(prompt):
    print(prompt, end="")
    value = input().strip()
    return value

def read_float(prompt):
    value = read_string(prompt)
    # Use float() to convert the string to a floating-point number
    return float(value)

def read_integer(prompt):
    value = read_string(prompt)
    # Use int() to convert the string to an integer
    return int(value)

def read_float(prompt):
    value = read_string(prompt)
    # Use float() to convert the string to a floating-point number
    return float(value)

def read_integer_in_range(prompt, minimum, maximum):
    print(prompt, end="")
    value = int(input().strip())
#   value = read_integer(prompt)
    while value < minimum or value > maximum:
        print(f"Please enter a value between {str(minimum)} and {str(maximum)}.")
        value = read_integer(prompt)
    return value    
  
# # Example usage:
# minimum_value = 1
# maximum_value = 10
# user_input = read_integer_in_range(f"Enter an integer between {minimum_value} and {maximum_value}: ", minimum_value, maximum_value)
# print("You entered:", user_input)


# user_input = read_integer("Enter a string: ")
# print("You entered:", user_input)  


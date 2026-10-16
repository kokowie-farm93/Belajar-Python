# Handling errors in Python
# Errors can be handled using try-except blocks.
print("=== Error Handling Example ===")
try:
    point1 = int(input("Enter the first point: "))
    point2 = int(input("Enter the second point: "))
    result = point1 / point2
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter numeric values.")
except ZeroDivisionError:
    print("Error: Cannot be zero.")    
except :
    print("Error in your calculation, please check your input.")
print("Program continues after error handling.")
print("--------")

# try-except-else-finally
try:
    point = int(input("Enter the point: "))
except ValueError:
    print("Invalid input. Please enter a numeric value.")
else:
    print("The point entered is:", point)
    if point > 0:
        print("The point is positive.")
    elif point < 0:
        print("The point is negative.")
    else:
        print("The point is zero.")
# if error , except block will be executed, if no error , else block will be executed.
finally:
    print("This block will always execute, regardless of whether an error occurred or not.")

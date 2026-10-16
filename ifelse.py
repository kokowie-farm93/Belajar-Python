# normal if else statement
numbers = int(input("Enter numbers : "))
if numbers > 0:
    result = "Positive"
elif numbers == 0:
    result = "Zero"
else:
    result = "Negative"
print(result)

point1 = int(input("Enter Point : "))
 # ternary operator
result1 = "Positive" if point1 > 0 else "Zero" if point1 == 0 else "Negative"
print(result1)

Point = int(input("Enter Point : "))
if Point >= 90:
    result = "A"
elif Point >= 80:
    result = "B"
elif Point >= 70:
    result = "C"
elif Point >= 60:
    result = "D"
else:
    result = "F"
print(result)

# logic operator
age = int(input("Enter Age : "))
license = input("Do you have a license? (yes/no): ")
if age >= 18 and license == "yes":
    print("You are eligible to drive.")
else:
    print("You are not eligible to drive.")

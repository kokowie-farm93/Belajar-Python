# "def"= keyword , space, then name,then ():

def hello_farm():
    print("Hello Kokowie Farm!")
# call function
hello_farm()
hello_farm()
hello_farm()

# parameter = value inside () , can be used to pass data to function
def nick_name(name):
    print("Hi", name)
    print("Nice to meet you")
# call function with parameter
nick_name("Kokowie")
nick_name("Regine")
nick_name("David")
nick_name("Ayumi")

def count_multiplication(a, b):
    result = a * b
    print("count_multiplication:", result)
count_multiplication(7, 8)
count_multiplication(4, 9)

# return = keyword to return value from function
def calculate_area(area):
    length = 20.5
    high = length * area * area
    return high
# call function with return value
count1 = calculate_area(4)
count2 = calculate_area(8)

print("calculate_area area 4", count1)
print("calculate_area area 8", count2)

# default parameter = value that will be used if no argument is given
def garden(name, fruit="Organic"):   # Organic = default parameter
  # "Organic" is used when no argument is given for fruit
    print(fruit, name)
# call function with default parameter
garden("Lettuce")
garden("Spinach", "Cabbage") # Default will be replaced if second argument has another value
garden("Carrot", "Potato")

 # Keyword Argument = Free Argument Order, can be used to call function with arguments in any order
def introduction(name, age, city):
    print("Name :", name)
    print("Age :", age)
    print("City :", city)

# Positional Argument = Arguments must be in the same order as the parameters
introduction("Koko",26, "Aceh")

# Free Argument Order = Arguments can be in any order, as long as the parameter name is specified
introduction(city="Medan", name="Kokowie", age=35)
introduction(age=24, city="Jakarta", name="Monica")

# Function with default parameter, keyword argument, and positional argument
def create_profile(name, age, city="Medan", job="Freelancer"):
    print(f"=== Profile {name.upper()} ===")  #name.upper means name will be printed in uppercase
    print(f"Age = {age} years old")
    print(f"City = {city}")
    print(f"Job = {job}")
    print("=========")

# Positional + Keyword Argument 
create_profile("Koko", 30)
create_profile("Tina", 18, job="Cashier")
create_profile("Gina", 27, city="Surabaya")

# LOCAL VARIABLE
def function_test():
    x = 10     # x = Local
    print("Value x is", x)
function_test()
#print(x) # can't access from outside variable, # because x is local variable, will cause error if uncommented

# Global Variable
name_global = "Kokowie"
def view_name():
    print("Name:", name_global)

# Change Global Variable
def change_name():
    global name_global
    name_global = "Chen"  # change global variable
    print("Local Name :", name_global)
view_name()
change_name()

def print_list(*list):  # *list = variable length argument, can accept multiple arguments
    for item in list:
        print(item)
print_list(1, 2, 3, 4, 5)
print_list("Kokowie", "Regine", "David", "Ayumi")
print("------------")

def print_dict(**dict):  # **dict = variable length keyword argument, can accept multiple keyword arguments
    for key, value in dict.items():
        print(key, ":", value)
print_dict(name="Kokowie", age=26, city="Aceh")
print_dict(name="Regine", age=24, city="Jakarta", job="Designer")
print_dict(name="David", age=30, city="Medan", job="Engineer", hobby="Gaming")
print_dict(name="Ayumi", age=28, city="Surabaya", job="Teacher", hobby="Reading", language="English")
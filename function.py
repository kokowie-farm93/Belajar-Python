# "def"= keyword , must have space, then name,then ():

def hello_farm():
    print("Hello Kokowie Farm!")

hello_farm()
hello_farm()
hello_farm()

# parameter
def nick_name(name):
    print("Hi", name)
    print("Nice to meet you")
nick_name("Kokowie")
nick_name("Regine")

def count_multiplication(a, b):
    result = a * b
    print("count_multiplication:", result)
count_multiplication(7, 8)
count_multiplication(4, 9)

def calculate_area(area):
    length = 20.5
    high = length * area * area
    return high
count1 = calculate_area(4)
count2 = calculate_area(8)

print("calculate_area area 4", count1)
print("calculate_area area 8", count2)

def garden(name, fruit="Organic"):   # Organic = default parameter
    print(fruit, name)
garden("Lettuce")            # "Organic" is used when no second argument is given
garden("Spinach", "Cabbage") # Default will be replaced if second argument has another value
garden("Carrot", "Potato")

 # Keyword Argument = Free Argument
def introduction(name, age, city):
     print("Name :", name)
     print("Age :", age)
     print("City :", city)

introduction("Koko",26, "Aceh")

introduction(city="Medan", name="Kokowie", age=35)
introduction(age=24, city="Jakarta", name="Monica")

def create_profile(name, age, city="Medan", job="Freelancer"):
    print(f"=== Profile {name.upper()} ===")
    print(f"Age = {age} years old")
    print(f"City = {city}")
    print(f"Job = {job}")
    print("=========")
create_profile("Koko", 30)
create_profile("Tina", 18, job="Cashier")
create_profile("Gina", 27, city="Surabaya")

# LOCAL VARIABLE
def function_test():
    x = 10     # x = Local
    print("Value x is", x)
function_test()
#print(x) # cant access from outside variable, cause Local Variable

# Global Variable
name_global = "Kokowie"
def view_name():
    print("Name:", name_global)

def change_name():
    global name_global
    name_global = "Chen"  # change global variable
    print("Local Name :", name_global)
view_name()
change_name()
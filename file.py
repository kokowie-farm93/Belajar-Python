# r=read, w=write, a=append, x=create
print("Save value data to a file")

file = open("students_point.txt", "w") #w=write

while True:
    name = input("Student name (Enter if done): ")
    if name == "":
        break
    point = input("Student point: ")

# Write the name and point to the file
    file.write(name + ", " + point + "\n") #file.write() is used to write data to the file
    print("Data",  name, "saved to file!")
file.close()
print("All data saved to students_point.txt!")
print("------")

#read the data from the file
file = open("students_point.txt", "r") #r=read

for line in file:
    data = line.strip().split(",")
    print(data[0], ":", data[1])
file.close()
print("All data read from students_point.txt!")
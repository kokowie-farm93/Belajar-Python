#save data in key-value{}

student = {"name": "David", "age": 18, "classroom": "8B" }
print(student)

print(student["name"])
print(student["age"])
print(student["classroom"])

#change
student["age"] = 20
print(student)

#del
del student["classroom"]
print(student)

for key in student:
    print(key, ":", student[key])  #key

for key, value in student.items():
    print(key, ":", value)  #key-value pairs
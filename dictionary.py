#save data in key-value{}
student = {"name": "David", "age": 18, "classroom": "8B" }
print(student)

print(student["name"])
print(student["age"])
print(student["classroom"])

#change value
student["age"] = 20
print(student)

#del
del student["classroom"]
print(student)

#iterate through keys
for key in student:
    print(key, ":", student[key])  #key

for key, value in student.items():
    print(key, ":", value)  #key-value
 #Complete Multiplication Table
print("Multiplication Table")
for i in range(1, 6):
    for j in range(1, 6):
        result = i * j
        print(i, "x", j, "=", result)
    print("======")
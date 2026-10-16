# Print only odd numbers
for i in range(20):
    if i % 2 == 0: # even number, divisible by 2 
        continue  # Skip even numbers
    print(i)      # odd numbers with continue = printed
                  # even numbers with continue = ignored / not printed
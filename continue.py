# Print only odd numbers
for i in range(20):
    if i % 2 == 0: # divisible by 2 
        continue  # Skip, go to next number
    print(i)      # Only odd numbers will appear
    # even numbers with continue = ignored / not printed
import itertools

# Create the set of characters (a-z, 0-9)
characters = [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]

# Generate all 4-letter combinations
combinations = itertools.product(characters, repeat=4)

# Open a file to save the combinations
with open('us.txt', 'w') as file:
    for combination in combinations:
        # Join the tuple into a string and write it to the file with a newline
        file.write(''.join(combination) + '\n')

print("Combinations have been saved to 'us.txt'")

def count_alphabet_occurrences(s):
    # Convert the string to uppercase to count case-insensitively
    s = s.upper()
    
    # Dictionary to store the count of each alphabet
    alphabet_count = {}
    
    # Iterate through each character in the string
    for char in s:
        if char.isalpha():  # Check if the character is an alphabet
            if char in alphabet_count:
                alphabet_count[char] += 1
            else:
                alphabet_count[char] = 1
    
    # Sort the dictionary by alphabet
    sorted_alphabet_count = dict(sorted(alphabet_count.items()))
    
    # Print the occurrences
    for char, count in sorted_alphabet_count.items():
        print(f"{char} - {count}")

# Examples
strings = ["namaskar india", "asish pradhan", "hello india"]

for string in strings:
    print(f"String: {string}")
    count_alphabet_occurrences(string)
    print()

def count_alphabet_occurrences(s):
    s = s.upper()
    occurrences = {}
    for char in s:
        if char.isalpha():
            if char in occurrences:
                occurrences[char] += 1
            else:
                occurrences[char] = 1
    return dict(sorted(occurrences.items()))
input_string = input("Enter a string: ")
occurrences = count_alphabet_occurrences(input_string)
print("\nOccurrences:")
for alphabet, count in occurrences.items():
    print(f"{alphabet} - {count}")
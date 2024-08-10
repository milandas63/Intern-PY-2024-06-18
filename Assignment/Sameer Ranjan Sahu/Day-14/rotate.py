def rotate_string(s):
    length = len(s)
    rotated_strings = []

    # Generate the rotated strings
    for i in range(length):
        rotated_string = s[-i:] + s[:-i]
        rotated_strings.append(rotated_string)

    return rotated_strings

# Example usage
input_string = "BOSS"
result = rotate_string(input_string)

# Print the result
for line in result:
    print(" ".join(line))

def print_number_pyramid(n):
    for i in range(1, n + 1):
        # Create the descending part of the pattern
        left_part = ''.join(str(j) for j in range(i, 0, -1))
        # Create the ascending part of the pattern
        right_part = ''.join(str(j) for j in range(2, i + 1))
        # Combine both parts to form the full pattern
        number_str = left_part + right_part
        # Center the pattern with respect to the maximum width
        print(number_str.center(2 * n - 1))

# Number of rows in the pyramid
n = 9
print_number_pyramid(n)
def print_number_pyramid(n):
    for i in range(1, n + 1):
        left_part = ''.join(str(j) for j in range(i, 0, -1))
        right_part = ''.join(str(j) for j in range(2, i + 1))
        number_str = left_part + right_part
        print(number_str.center(2 * n - 1))

n = 9
print_number_pyramid(n)
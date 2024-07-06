def print_number_pyramid(n):
    for i in range(n):
        number_str = str(i) * (2 * i + 1)
        print(number_str.center(2 * n - 1))

# Number of rows in the pyramid
n = 10
print_number_pyramid(n)
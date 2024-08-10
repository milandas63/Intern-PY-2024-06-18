space=10
def print_palindrome_pyramid(n):
    for i in range(n):
        half = ''.join(chr(97 + j) for j in range(i + 1))
        palindrome = half + half[-2::-1]
        print(palindrome.center(2 * n - 1))

# Number of rows in the pyramid
n = 10
print_palindrome_pyramid(n)
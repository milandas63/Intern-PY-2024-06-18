def generate_pattern(n):
    for i in range(n):
        print(' ' * (n - i - 1), end='')
        
        for j in range(i + 1):
            print(chr(97 + j), end='')
        
        for j in range(i - 1, -1, -1):
            print(chr(97 + j), end='')
        
        print()

n = 10
generate_pattern(n)
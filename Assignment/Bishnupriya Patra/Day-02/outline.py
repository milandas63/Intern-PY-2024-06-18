height = 10  # You can change the height of the triangle here

for i in range(height):
    if i == height - 1:  # Last row
        print('*' * (2 * height - 1))
    else:
        # Print leading spaces
        print(' ' * (height - i - 1), end='')
        
        # Print the first star
        print('*', end='')
        
        if i > 0:  # For rows other than the first
            # Print spaces between the first and last star
            print(' ' * (2 * i - 1), end='')
            
            # Print the last star
            print('*')
        else:
            print()  # Move to the next line after the first star

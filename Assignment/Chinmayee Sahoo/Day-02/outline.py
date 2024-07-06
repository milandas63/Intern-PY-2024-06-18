def print_triangle_outline(height):
    for row in range(height):
        for col in range(height):
            # Print star for the first row
            if row == 0:
                if col == 0:
                    print('*', end='')
                else:
                    print(' ', end='')
            # Print stars for the last row
            elif row == height - 1:
                print('*', end='')
            # Print stars for the first and last columns of intermediate rows
            else:
                if col == 0 or col == row:
                    print('*', end='')
                else:
                    print(' ', end='')
        print()

# Example usage:
height = 5
print_triangle_outline(height)
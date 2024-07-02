def unisum(number):
    while number >= 10:
        number = sum(int(digit) for digit in str(number))
    return number

# Test cases
print(f"Unisum of 728394 is {unisum(728394)}")       # Output: 6
print(f"Unisum of 9778911223 is {unisum(9778911223)}") # Output: 4
print(f"Unisum of 7978168568 is {unisum(7978168568)}") # Output: 2

# Additional test cases
print(f"Unisum of 123456 is {unisum(123456)}")       # Output: 3
print(f"Unisum of 987654321 is {unisum(987654321)}")   # Output: 9

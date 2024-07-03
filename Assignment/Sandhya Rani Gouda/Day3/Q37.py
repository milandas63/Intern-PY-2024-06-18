def add(number):
    while number >=10:  
        number = sum(int(digit) for digit in str(number))  
    return number
print(add(728394))  
print(add(9778911223))  
print(add(7978168568))  
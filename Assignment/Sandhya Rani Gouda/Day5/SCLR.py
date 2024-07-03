"""
    =   Take two numbers from the keyboard
        Display a menu with Add, Subtract, Multiply and Divide
        On selecting the action the two number are performed accordingly
            >   Use input() function to take the number form keyboard

"""
def add(x,y):
    print(x)
    print(y)
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

try:
    print("Simple Calculator")
    first_number = int(input("Enter the 1st number: "))
    second_number = int(input("Enter the 2nd number: "))
    print("MENU")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print()
    choice = int(input("Enter action to perform: "))
    #choice = input("Enter action to perform: ")
    print()
    if choice==1:
        print(add(first_number, second_number))
    elif choice==2:
        print(subtract(first_number, second_number))
    elif choice==3:
        print(multiply(first_number, second_number))
    elif choice==4:
        print(divide(first_number, second_number))

except ValueError:
	print('Input value is invalid')
except ZeroDivisionError:
	print('Denominator must no be number')
except SyntaxError:
	print('The choice value is not appropriate')
except Exception as e:
	print(e.__class__.__name__,'input value is invalid')
else:
	print('This line is printed when there is no exception')
finally:
	print('Must be printed')
    
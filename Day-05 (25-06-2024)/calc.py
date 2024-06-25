"""
Write a program in Python to receive 2 int numbers and show the following menu. 
Take the choice from the keyboard and perform the operation?

	Enter first INT number: 
	Enter second INT number: 

	1.  Addition
	2.  Subtraction
	3.  Multiplication
	4.  Division

	Enter choice: 
"""
def Addition(x,y):
	return x+y

def Substraction(x,y):
	return x-y

def Multiplication(x,y):
	return x*y

def Division(x,y):
	return x/y

try:
	n1 = int(input('Enter first INT number:  '))
	n2 = int(input('Enter second INT number: '))
	print()
	print('1.  Addition')
	print('2.  Substraction')
	print('3.  Multiplication')
	print('4.  Division')
	print()
	choice = int(input('Enter Choice: '))

	if choice==1:
		print('Sum of the number is',Addition(n1,n2))
	elif choice==2:
		print('Substraction of the number is',Substraction(n1,n2))
	elif choice==3:
		print('Productuct of the number is',Multiplication(n1,n2))
	elif choice==4:
		print('Division of the number is',Division(n1,n2))
	else:
		#print('Unknown choice!!!')
		raise ArithmeticError('Invalid choice!')
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

try:
	arithmetic = 5/1
	print(arithmetic)
except ArithmeticError:
  print('Arithmetic: This is divided by zero error')
except ZeroDivisionError:
  print('ZeroDivision: This is divided by zero error')
except IndexError:
  print('Indices is out of range error')
finally:
  print('Finally executes in all situation')

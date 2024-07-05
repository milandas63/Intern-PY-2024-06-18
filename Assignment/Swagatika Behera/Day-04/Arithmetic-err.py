def division(dividend, divisor):
    try:
        result = dividend / divisor
        print("Result:", result)
    except ArithmeticError:
        print("Error: Arithmetic error occurred!")
dividend = float(input("Input the dividend: "))
divisor = float(input("Input the divisor: "))
division(dividend, divisor) 
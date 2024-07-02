def arithmetic_error_example():
    try:
        result = 10 / 0
    except ArithmeticError as e:
        print(f"ArithmeticError caught: {e}")

arithmetic_error_example()

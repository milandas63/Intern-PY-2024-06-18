import decimal

def floating_point_error_example():
    decimal.getcontext().traps[decimal.FloatOperation] = True
    try:
        result = 1.0 / 0.0
    except FloatingPointError as e:
        print(f"FloatingPointError caught: {e}")

floating_point_error_example()

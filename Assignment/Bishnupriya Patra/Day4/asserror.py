def assertion_error_example():
    try:
        assert 2 + 2 == 5, "Math is wrong!"
    except AssertionError as e:
        print(f"AssertionError caught: {e}")

assertion_error_example()

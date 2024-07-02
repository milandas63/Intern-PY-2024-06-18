def exception_example():
    try:
        raise Exception("This is a generic exception")
    except Exception as e:
        print(f"Exception caught: {e}")

exception_example()

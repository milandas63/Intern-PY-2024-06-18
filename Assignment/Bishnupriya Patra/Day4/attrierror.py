def attribute_error_example():
    class MyClass:
        pass

    obj = MyClass()
    try:
        obj.some_attribute
    except AttributeError as e:
        print(f"AttributeError caught: {e}")

attribute_error_example()

def key_error_example():
    my_dict = {'a': 1, 'b': 2}
    try:
        print(my_dict['c'])
    except KeyError as e:
        print(f"KeyError caught: {e}")

key_error_example()
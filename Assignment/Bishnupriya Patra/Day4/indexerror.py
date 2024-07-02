def index_error_example():
    my_list = [1, 2, 3]
    try:
        print(my_list[5])
    except IndexError as e:
        print(f"IndexError caught: {e}")

index_error_example()

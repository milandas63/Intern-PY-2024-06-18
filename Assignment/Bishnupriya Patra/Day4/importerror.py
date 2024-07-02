def import_error_example():
    try:
        import non_existent_module
    except ImportError as e:
        print(f"ImportError caught: {e}")

import_error_example()

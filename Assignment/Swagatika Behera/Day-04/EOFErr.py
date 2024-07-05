def eof_error_example():
    try:
        input("Press Ctrl+D (or Ctrl+Z on Windows) to trigger EOFError: ")
    except EOFError as e:
        print(f"EOFError caught: {e}")

eof_error_example()
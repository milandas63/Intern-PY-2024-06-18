def indentation_error_example():
    try:
        exec("""
def foo():
print("This will cause an IndentationError")
""")
    except IndentationError as e:
        print(f"IndentationError caught: {e}")

indentation_error_example()

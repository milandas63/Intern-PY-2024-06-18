def keyboard_interrupt_example():
    try:
        while True:
            pass
    except KeyboardInterrupt as e:
        print(f"KeyboardInterrupt caught: {e}")

keyboard_interrupt_example()

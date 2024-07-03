def frame(strings):
    max_length = max(len(string) for string in strings)
    
    border = '*' * (max_length +4)
    
    print(border)
    
    for string in strings:
        print(f"* {string.ljust(max_length)} *")
    
    print(border)


strings = ["Hello", "World", "in", "a", "frame"]
frame(strings)
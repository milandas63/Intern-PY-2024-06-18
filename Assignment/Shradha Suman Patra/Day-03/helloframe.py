def print_in_frame(words):
    max_length = max(len(word) for word in words)
    border = '*' * (max_length + 4)
    
    print(border)
    for word in words:
        print(f"* {word.ljust(max_length)} *")
    print(border)

# Test case
words_list = ["Hello", "World", "in", "a", "frame"]
print_in_frame(words_list)
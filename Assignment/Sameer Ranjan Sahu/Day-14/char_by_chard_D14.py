def read_file_character_by_character(file_path):
    with open(file_path, 'r') as file:
        while True:
            char = file.read(1)  
            if not char:
                break  
            print(char, end='')

file_path = 'path_to_your_file.txt'
read_file_character_by_character(file_path)

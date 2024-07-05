def number_to_words(number):
    digit_to_word = {
        '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
        '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'
    }
    
    number_str = str(number)
    
    words = []
    
    for digit in number_str:
        words.append(digit_to_word[digit])
    
    return ' '.join(words)


print(number_to_words('12345'))
print(number_to_words('03786')) 
print(number_to_words('72913'))  

text = 'Hello Students, we are learning Python'
vowels = 'AEIOUaeiou'

count = 0
for i in range(0,len(text)):
	v = text[i]
	for j in range(0,len(vowels)):
		if(vowels[j]==v):
			count = count+1
			break

print('Total number of vowels are ',count)

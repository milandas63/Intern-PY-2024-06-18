import time

try:
	with open('file.txt', 'r') as fp:
		for part in iter(lambda: fp.read(1), ''):
			print(part, end=' ')
			time.sleep(0.125)
		fp.close()

except Exception as e:
	print('Some error',e.__class__.__name__)
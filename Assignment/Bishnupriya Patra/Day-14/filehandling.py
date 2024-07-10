try:
	content = ""

	# open(path, flags, mode=511, *, dir_fd=None)
	with open('file.txt','r') as handle:
		content = handle.read()
		#print(content)
		handle.close()

	with open('copyfile.txt','w') as f:
		#print('2: ',content)
		f.write(content)
		f.close()

except Exception as e:
	print(e.__class__.__name__)
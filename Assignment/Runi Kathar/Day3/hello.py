triangle(10)
  for i in range(1, height +1):
    alphabets=''.join (chr(64+x)for x in range(1,i+1))
    palindromic_alphabets=alphabets+alphabets[-2::-1]
    print(palindromic_alphabets.center(2*height-1))
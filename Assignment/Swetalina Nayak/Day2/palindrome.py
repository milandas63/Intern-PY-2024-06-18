sp = 40
for i in range(1,10):
        for j in range(0,sp):
           print(' ',end=' ')
        for j in range(1,(i+1)):
            print(j,end=' ')
        for j in range(i-1,0,-1):
                print(j,end=' ')
        print()
        sp=sp-1
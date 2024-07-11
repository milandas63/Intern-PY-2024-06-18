import stretcher as s

start = 2
end = 41

for m in range(start, end+1, +5):
    for n in range(1, 11):
        for o in range(m, m+5):
            print(s.justR(o,2),"x",s.justR(n,2),"=",s.justR((o*n),3),"  ", end="")
        print()
    print()
print()
print()
print()

print(s.justR(100,15))
print(s.justC(100,15))
print(s.justL(100,15))
print(s.replicate("=",80))

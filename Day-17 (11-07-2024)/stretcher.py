def justR(n, l):
    r = str(n)
    for i in range(len(r), l):
        r = " "+r
    return r

def justL(n, l):
    r = str(n)
    for i in range(len(r), l):
        r = r+" "
    return r

def justC(n, l):
    r = str(n)
    for i in range(len(r), l):
        if i%2==0:
            r = r+" "
        else:
            r = " "+r
    return r

def replicate(char, times):
    r = ""
    for i in range(0, times):
        r = r + char
    return r;

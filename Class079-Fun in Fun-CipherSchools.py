def great_2(a,b):
    if a>b:return a
    return b

def great1_3(a,b,c):
    if a>b and a>c: return a
    elif b>c and b>a: return b
    else : return c

def great2_3(a,b,c):
    # M-1
    # big=great_2(a,b)
    # return great_2(big,c)
    # M-2
    return great_2(great_2(a,b),c)

#! kiss-Keep it simple stupid

print(great2_3(int(input()),int(input()),int(input())))

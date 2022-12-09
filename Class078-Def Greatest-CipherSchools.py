
def great_3(a,b,c):
    if a>b and a>c: return a
    elif b>c and b>a: return b
    else : return c
print(great_3(int(input()),int(input()),int(input())))

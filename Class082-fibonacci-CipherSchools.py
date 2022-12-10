def fibonacci(a,b,n):
    # a=0     #! First Num
    # b=1     #! Second Num
    if n == 1:print(a)
    elif n==2:print(a,b) 
    else:
        print(a,b,end=" ")
        for i in range (n-2):
            c=a+b
            a=b
            b=c
            print(b,end=" ")
            
a=int(input("Start 1 : "))
b=int(input("Start 2 : "))
n=int(input("No of : "))
fibonacci(a,b,n)
        
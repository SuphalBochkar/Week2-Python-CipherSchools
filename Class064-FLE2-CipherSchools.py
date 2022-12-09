# For loop
# Sum of digits

tot=0
tot1=0
n=input("Num: ")
for i in n:
    tot+=int(i)
for i in range(len(n)):
    tot1+=int(n[i])

print(tot)
print(tot1)
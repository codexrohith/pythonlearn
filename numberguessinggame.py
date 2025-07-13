import random
n = random.randint(1,100)
t=0
while True :
    t+=1
    op=int(input(("Enter a number between 1 and 100 : ")))
    if op < n:
        print("LOW Try again")
    elif op > n:
        print("HIGH Try again")
    else:
        break
print(f"CONGRAGULATIONS!! You have found {n} in {t} turns")
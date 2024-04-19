x = 2

y = 4
if x>0:
    print('x is positive')


if x%2==0:
    print('x is even')
else:
    print('x is odd')

# Chain conditional
if x<y:
    print('x is less than y')
elif x>y:
    print('x is greater than y')
else:
    print('x and y are equal')

#NESTED CONDITION
if x==y:
    print('x is less than y')
else:
    if x<y:
        print('x is less than y')
    else:
        print('x is greater than y')

#Recursion
def countdown(n):
    if n<= 0:
        print('Blastoff')
    else:
        print(n)
        countdown(n-1)

countdown(5)
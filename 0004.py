#calculator using loops and conditions
while True :
    a=int(input('Enter a number: '))
    b=input('Enter a operator: ')
    c=int(input('Enter a number: '))
    if b=='+':
        print(a+c)
    elif b=='-':
        print(a-c)
    elif b=='*': 
        print(a*c)
    elif b=='/':
        print(a/c)
    else:
        print('Invalid operator')

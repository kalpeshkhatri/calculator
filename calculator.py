print('for sumation operation:+')
print('for substraction operation:-')
print('for multiplication operation:*')
print('for divistion operation:/')
print('for percentage operation:%')



while True:
    O=input('enter operation:')
    

    a=float(input('enter the number1:'))
    b=float(input('enter the number2:'))
    if O=='+': #sumation
        print(a+b)
    elif O=='-': #substaction
        print(a-b)
    elif O=='*': #multiplication
        print(a+b)

    elif O=='/':#division
        if b==0:
            print('error because b should not be 0')
        else:    
            print(a+b)

    elif O=='%':#percentage
        print(b,'% percentage of',a,'=',(a*b*0.01))

    else:
        print('operation is invalid')
    x=input('do you want to do next operation?(yes/no):')
    if x!='yes':
        break

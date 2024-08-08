import random
print('Guess the random number from 1 to 100.\nif your guess is right you will get 50 point, per one wrong guess your points will deduct 10 points.\n If your guess correct under 5 trial then you will get bonus point 50.\nyou get 1000 points in starting.')

n=random.randint(1,100)
point=1000
count=0

while True:
    count=count+1
    try:
        num=int(input('Guess Number:'))
    except:
        print('invalid input')
        break
    if num==n:
        point=point+50
        if count<=5:
            point=point+50
            print('your guess is correct under 5 trial. You won bonus points 50.your points is:',point)
        else:
            print('your guess is correct','and your point is:',point)
        x=input('are you want to play again?(yes/no):')
        if x.lower()=='yes':
            count=0
            n=random.randint(1,100)
        else:
            print('your total trials is:',count,'your final point is:',point)
            break
    elif num<n:
        point=point-10
        print('your guess is less than right value','and your points is:',point)
    else:
        point=point-10
        print('your guess is greater than right value','and your points is:',point)

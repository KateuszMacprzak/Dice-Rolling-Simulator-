import random
name=input('Enter your name: ')
print('Welcome in dice rolling simulator %s'%name)
x='y'
while (x=='y'):
    a=random.randint(1,6)
    if (a==1):
        print('___')
        print('   ')
        print(' 0 ')
        print('   ')
        print('___')
    elif (a==2):
        print('___')
        print(' 0 ')
        print(' 0 ')
        print('   ')
        print('___')
    elif (a==3):
        print('___')
        print(' 0 ')
        print(' 0 ')
        print(' 0 ')
        print('___')
    elif (a==4):
        print('___')
        print('0 0')
        print('   ')
        print('0 0')
        print('___')
    elif (a==5):
        print('___')
        print('0 0')
        print(' 0 ')
        print('0 0')
        print('___')
    else:
        print('___')
        print('000')
        print('000')
        print('000')
        print('___')
    x=input('Enter y if you want to roll once again or n if you want to exit...')
    if (x=='n'):
        print('Thanks for your time, have a nice day %s'%name)
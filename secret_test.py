password = 'a123'
frequency = 3
while frequency > -1:
    password_test = input('Please test to answer my password：')
    if password == password_test:
        print('congratulations! Answer my password!')
        break
    else:
        if frequency > 1:
            print('You have' ,frequency ,'chances!')
            frequency = frequency - 1
        elif frequency == 1:
            print('You have' ,frequency ,'chance!!!')
            frequency = frequency - 1
        else:
            print('Sorry,you don\'t answer my password!' )
            frequency = frequency - 1
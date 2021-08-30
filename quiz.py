print('Welcome.')

points = 0

playing = input('Are you ready? Press Y for Yes and N for No ')

if playing == 'N':
    quit()
elif playing == 'n':
    quit()
else :
    print('Welcome to quiz competition')
    print('your score {}'.format(points))

#question one

answer = input('What is the capital of India?  ')

if answer != "new delhi":
    print('Wrong answer. Your score is {}'.format(points))
    quit()
elif answer == 'new delhi':
    points +=1
    print('Correct answer. Your score is {}'.format(points))

#question two

answer = input('How many states are there in India?  ')

if answer != "29":
    print('uffff. Try again. Your score is {}'.format(points))
    quit()
elif answer == '29':
    points +=1
    print('Very good. Your score is {}'.format(points))


#question three

answer = input('How many union territories are there in India?  ')

if answer != "7":
    print('Too bad. Try again. Your score is {}'.format(points))
    quit()
elif answer == '7':
    points +=1
    print('Very good. Your score is {}'.format(points))

#question four

answer = input('Who is the prime minister of India?  ')

if answer != "narendra modi":
    print('Very close. Try again. Your score is {}'.format(points))
    quit()
elif answer == 'narendra modi':
    points +=1
    print('Very good. Your score is {}'.format(points))

#question five

answer = input('Who is the president of India?  ')

if answer != "ramnath govind":
    print('Almost there. Try again. Your score is {}'.format(points))
    quit()
elif answer == 'ramnath govind':
    points +=1
    print('Very good. Your score is {}'.format(points))
    print('Congratulation. You scored 5/5')
    quit()
    
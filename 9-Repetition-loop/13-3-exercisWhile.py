
#question  = input('Which city is called the city of love?')
answer = 'PARIS'
answerOfUser = ''
count = 0
lose = False

while answer!= answerOfUser and not lose:

    if count < 3 :
       answerOfUser  = input('Which city is called the city of love?')
       count += 1
    else:
     lose = True
if lose:
    print('you lose')

else:
    print('you win')


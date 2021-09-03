number_to_guess = 8
chances = 0
won = False

print('Number Guessing Game')
print('Guess a number (between 1 and 9)')

while chances < 5:
    guessed_number = int(input('Enter Your Guess:- '))
 
    if (guessed_number == number_to_guess):
        won = True
        break
    else:
        if(guessed_number>number_to_guess+5):
            print(guessed_number, ', Too high')
        elif(guessed_number<number_to_guess-5):
            print(guessed_number, ', Too Low')
        elif(guessed_number<number_to_guess+5 and guessed_number>number_to_guess):
            print(guessed_number, ', Very Near But Still High')
        elif(guessed_number>number_to_guess-5 and guessed_number<number_to_guess):
            print(guessed_number, ', Very Near But Still Low')

        print('Try Guessing a Different Number...')

    chances +=1



if (won == False):
    print('You Loose')
    print('Thankyou For Playing')
else:
    print('You Win!!')
    print('Thankyou For Playing')

close = input('You Can Quit Now')
Name=input('Enter Your Name: ')
print('Welcome to the Number Guessing Game,', Name + ' ' + '==>Choose a number from 1 to 100. Good luck winning, player!')
import random
number = random.randint(1, 100)
ready = input('Ready for a game of life and death? (y/n): ')
if ready.lower() == 'y':
    print(f'Welcome to hell, {Name}')
else:
    print('You are a coward,', Name + ' ' + '==>Goodbye!')
    exit()
Number=input('Enter a random door number from 1 to 100 : ')
The_door_of_life=3,13,14,2,9,6
if int(Number) not in The_door_of_life:
    print(f'You died,{Name}')
    print ('Do you want another chance? (y/n): ')
    if input().lower() == 'y':
        print(f'You have been given another chance,', Name + ' ' + '==>Good luck!')
        Number = int(input('Enter another number between 1 and 100: '))
    if int(Number)  in The_door_of_life:
        print(f'You survived,{Name}')
    else:
     print('You are a coward,', Name + ' ' + '==>Goodbye!')
     exit()
Attempts=0
while True:
    guess = int(input('Guess the number (1-100): '))
    Attempts += 1
    if guess < number:
        print('Too low!')
    elif guess > number:
        print('Too high!')
    else:
        print(f'Correct! You won in {Attempts} attempts, {Name}!')
        break
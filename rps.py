'''
Rock Paper Scissors
-------------------------------------------------------------
'''

import random
import os
import re


def check_play_status():
    valid_responses = ['yes', 'no']
    while True:
        try:
            response = input('Do you wish to play again? (Yes or No): ')
            if response.lower() not in valid_responses:
                raise ValueError('Yes or No only')

            if response.lower() == 'yes':
                return True
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Thanks for playing!')
                exit()
        except ValueError as err:
            print(err)


def play_rps():
    wins = 0
    losses = 0
    ties = 0
    brain_farts = 0

    play = True
    while play:
        # os.system('cls' if os.name == 'nt' else 'clear')
        # print('')
        print('Rock, Paper, Scissors - Shoot!')

        user_choice = input('Choose your weapon'
                            ' [R]ock], [P]aper, or [S]cissors: ')
        user_choice = user_choice.upper()
        if (user_choice =='') or (user_choice not in 'SsRrPp'):
            print('You\'re a stupid f*cking idiot')
            print('and should choose something that is actually R, P, or S!')
            brain_farts += 1
        choices = ['R', 'P', 'S']
        opp_choice = random.choice(choices)

        print(f'You chose: {user_choice}')
        print(f'I chose:   {opp_choice}')

        happy_face_message = 'You win!'
        # insult = 'You are a stupid fat f*cking loser!'
        insult = 'You don\'t have a brain and should work at the gym more so you can win 50/50s!'

        if user_choice == opp_choice:
            print(f'It\'s a tie! (But still {insult}!)')
            ties += 1
        if user_choice == 'S' and opp_choice == 'P':
            print(happy_face_message)
            wins = wins + 1
        if user_choice == 'S' and opp_choice == 'R':
            print(insult)
            losses += 1
        if user_choice == 'R' and opp_choice == 'P':
            print(insult)
            losses += 1
        if user_choice == 'R' and opp_choice == 'S':
            print(happy_face_message)
            wins += 1
        if user_choice == 'P' and opp_choice == 'S':
            print(insult)
            losses += 1
        if user_choice == 'P' and opp_choice == 'R':
            print(happy_face_message)
            wins += 1

        print('-' * 55)
        print(f'wins: {wins}, losses: {losses}, ties: {ties}, brain_farts: {brain_farts}')
        print('-' * 55)
        play = True


if __name__ == '__main__':
    play_rps()
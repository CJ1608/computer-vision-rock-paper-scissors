

import random


def play():   
    """call all the other three functions you've created (get_computer_choice, get_user_choice, and get_winner)"""  
    print('h1')
    
    def get_computer_choice():
        """randomly pick an option between "Rock", "Paper", and "Scissors" and return the choice"""
        computer_options = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(computer_options)
        print(computer_choice)
        #return computer_choice

    def get_user_choice():
        """ask the user for an input and return it"""
        user_choice = input(("Please enter your choice of either:\nRock, \nPaper, \nScissors: ")).casefold().strip() 
        print(user_choice)
        #return user_choice
                
    def get_winner(computer_choice, user_choice):
        """chose winner based on rules of rock paper scissors: rock beat scissors, paper beat rock, scissors beat paper"""
        winner = str()
        #tie
        if computer_choice == user_choice:
            print(f'You chose "{user_choice}" and your opponent chose "{computer_choice}"./t It\'s a tie!') 
        #computer wins
        elif (computer_choice == 'rock' and user_choice == 'scissors') or (computer_choice == 'paper' and user_choice == 'rock') or (computer_choice == 'scissors' and user_choice == 'paper'):
            print(f'You chose "{user_choice}" and your opponent chose "{computer_choice}"./t You lost')
            winner = 'Opponent'
            return winner
        #user wins
        elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
            print(f'You chose "{user_choice}" and your opponent chose "{computer_choice}"./t You won!')
            winner = 'User'
            return winner
        #shouldn't run
        else:
            print('Error.')
            
    get_computer_choice()
    print('h2')
    get_user_choice()
    print('h3')
    get_winner()
    print('h4')

play()

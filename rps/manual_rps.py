
import random

def play():   
    """Calls the other three functions get_computer_choice, get_user_choice, and get_winner to play game of rock, paper, 
    scissors. Prints the appropriate message to the user based on the outcome from get_winner method. 
    """
    
    def get_computer_choice():
        """Randomly picks an option from a list of "Rock", "Paper", and "Scissors" and returns the choice. 

        Returns:
            str: one item from computer_options list, used in get_winner method. 
        """
        computer_options = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(computer_options)
        return computer_choice
    
    def get_user_choice():
        """Asks the user for an input until it gets input that it can accept (that it is either rock, paper or scissors) 
        and returns it. 

        Returns:
            str: user choice of either rock, paper or scissors, used in get_winner method.
        """
        user_choice_accepted = False
        #loops until gets correct input
        while user_choice_accepted == False:
            #prompt user 
            user_choice = input(("\nPlease enter your choice of either rock, paper or scissors: ")).casefold().strip()
            #if it's not okay, ask to re-enter
            if user_choice not in ['rock', 'paper', 'scissors']:
                print('\nError. Try again')
                user_choice_accepted = False
            #if it is okay, return it     
            elif user_choice in ['rock', 'paper', 'scissors']:
                user_choice_accepted = True
                return user_choice
            #shouldn't run 
            else:
                print('Error')
            
    def get_winner(computer_choice, user_choice):
        """Chooses winner based on rules of rock paper scissors: rock beat scissors, paper beat rock, scissors beat paper 
        and prints appropriate message to the user. 

        Args:
            computer_choice (str): random computer choice of rock/paper/scissors from list, passed from get_computer_choice method.
            user_choice (str): user input of rock/paper/scissors, passed from get_user_choice method.
        """
        #tie
        if computer_choice == user_choice:
            print(f'You chose "{user_choice}" and your opponent chose "{computer_choice}". It\'s a tie!\n') 
        #computer wins
        elif (computer_choice == 'rock' and user_choice == 'scissors') or (computer_choice == 'paper' and user_choice == 'rock') \
            or (computer_choice == 'scissors' and user_choice == 'paper'):
            print(f'You chose "{user_choice}" and your opponent chose "{computer_choice}". You lost.\n')
        #user wins
        elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') \
            or (user_choice == 'scissors' and computer_choice == 'paper'):
            print(f'You chose "{user_choice}" and your opponent chose "{computer_choice}". You won!\n')
        #shouldn't run
        else:
            print('Error.')
    
    #calls 3 methods
    get_winner(computer_choice=get_computer_choice(), user_choice=get_user_choice())

#main call
play()
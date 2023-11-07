
import random
import time

import cv2
from keras.models import load_model
import numpy as np

class RPS:
    """
    The class is used to represent a game of RPS between computer and user webcam that finishes once the user or computer has won 3 times. 
    """
    
    def __init__(self):
        """
        See help(RPS) for more detail.
        """
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.user_wins = 0
        self.computer_wins = 0
    
    def play(self):   
        """
        This function is the main method that calls __countdown(), __get_computer_choice(),
        __get_prediction() and __get_winner. 
        
        It calls the methods mentioned until either the computer or user has won 3 games and prints
        a message showing the results to the user. It then closes the webcam. 
        """
        self.user_wins = 0
        self.computer_wins = 0
        while(self.user_wins < 3) and (self.computer_wins < 3):
            print(f'\nComputer: {game.computer_wins}\tUser: {game.user_wins}')
            self.__countdown()
            user_choice = self.__get_prediction()
            self.__get_winner(computer_choice=self.__get_computer_choice(), user_choice = user_choice)
        print(f'\tEnd of game! \nComputer: {game.computer_wins} \tUser: {game.user_wins}\n')
        # After the loop release the cap object
        game.cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
           
    def __get_computer_choice(self):
        """
        This function randomly picks an option from a list of "Rock", "Paper", and "Scissors" and 
        returns the choice. 

        Returns:
            str: one item from computer_options list, used in get_winner method. 
        """
        computer_options = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(computer_options)
        return computer_choice

    def __countdown(self):
        """
        This function generates a countdown to tell the user to show their hand (showing rock, paper or
        scissors) on the count of 0. 
        """
        start_time = time.time()
        counter = 5
        print('Please show your hand on 0')
        #while counter is between 5 and 0
        while counter >= 0:
            #while start_time plus a second is bigger than the current time- do nothing/waits for a second 
            while start_time + 1 > time.time():
                pass
            print(counter)
            counter -= 1
            #update time to new snapshot
            start_time = time.time()
        #when counter hits 0 it takes input in as answer
        print('Show your choice now...')

    def __get_prediction(self):
        """
        This function gets the user choice from the users camera and returns it to the __get_winner method. 
        
        The model is initalised in the init method. The model is what takes in the images from users camera. 
        The prediction is the numerical label returned from the model, representing which option the model thinks is shown. 
        Using argmax and a dictionary of keys(numerical label):value(nothing, rock, paper,scissors), the method returns the
        value to the __get_winner method. 
        
        Returns:
            str: user choice from user webcam
        """
        #make camera take in input for a second
        finish_time = time.time() + 1
        while time.time() < finish_time: 
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 
            self.data[0] = normalized_image
            prediction = self.model.predict(self.data)
            cv2.imshow('frame', frame)
            # Press q to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        #labels from model prediction
        labels = {0: 'nothing', 1: 'rock', 2:'paper', 3:'scissors'}
        answer = np.argmax(prediction)
        user_choice = labels.get(answer) 
        return user_choice
     
    def __get_winner(self, computer_choice, user_choice):
        """
        Takes in user and computer choice options from __get_computer_choice and __get_prediction methods.
        It prints an appropriate message depending on whether the user or computer has won and increases the
        number of computer_wins or user_wins variables. 

        Args:
            computer_choice (str): computers choice of r/p/s from __get_computer_choice 
            user_choice (str): users choice of nothing/r/p/s from __get_prediction
        """
        if user_choice == 'nothing':
            print(f'\nYou chose {user_choice}. Please try again.\n')
        elif computer_choice == user_choice:
            print(f'\nYou chose "{user_choice}" and your opponent chose "{computer_choice}". It\'s a tie!\n') 
        elif (computer_choice == 'rock' and user_choice == 'scissors') or (computer_choice == 'paper' and user_choice == 'rock') \
            or (computer_choice == 'scissors' and user_choice == 'paper'):
            print(f'\nYou chose "{user_choice}" and your opponent chose "{computer_choice}". You lost.\n')
            self.computer_wins += 1
        else:
            print(f'\nYou chose "{user_choice}" and your opponent chose "{computer_choice}". You won!\n')
            self.user_wins += 1


game = RPS()
game.play()
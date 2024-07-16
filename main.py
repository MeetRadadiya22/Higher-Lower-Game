from data import data
from art import logo, vs
import random
import os

data_A = {}
data_B = {}
result = 0

#this while loop is main while loop which will run till the user gives true answer. 
game = True
while game == True:
  selection = True
  #checks if both the data is similar then it will choose again from the list.
  while selection == True:
    data_A = random.choice(data)
    data_B = random.choice(data)

    if data_A == data_B:
      selection = True
    else:
      os.system('cls')
      selection = False
      print("h")
      print(logo)
      print(f"Compare A: {data_A['name']}, {data_A['description']}, from {data_A['country']}")

      print(vs)

      print(f"Compare B: {data_B['name']}, {data_B['description']}, from {data_B['country']}")
      
      # print(data_A['follower_count'])
      # print(data_B['follower_count'])
      

      #function which checks the highest followers
      def highest_follower():
        if data_A['follower_count'] > data_B['follower_count']:
          return "A"
        elif data_B['follower_count'] > data_A['follower_count']:
          return "B"

      #while loop to let the user type again if he fails.
      user_typo = True
      while user_typo == True:
        print(f"\nYour score: {result}")
        user_answer = input("Who has more followers? Type 'A' or 'B': ")
        #now lets check if the user guessed it right or not
        if user_answer == "A" or user_answer == "B":
          user_typo = False
          if user_answer == highest_follower():
            result += 1
            os.system('cls')
            
          else:
            game = False
            print(f"\nSorry that's wrong, your final score is {result}.")
        else:
          print("\nINVALID INPUT! Try again.\n")

    

     



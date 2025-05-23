import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock ,paper ,scissors]

user_choice = int(input("What do you choice? Type 0 for rock , 1 for paper, 2 for scissor\n"))

if user_choice >=0 and user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0 , 2)
print("Computer choice:")
print(game_images[computer_choice])

if user_choice >=3 or user_choice < 0 :
    print("You writed wrog number! You lose")
elif user_choice == 0 and computer_choice == 2 :
    print("You win!")
elif computer_choice == 0 and user_choice == 2 :
    print("You Lost!")
elif computer_choice > user_choice :
    print("You lost!")
elif user_choice > computer_choice:
    print("You win!")
elif user_choice == computer_choice :
    print("It's a draw !")

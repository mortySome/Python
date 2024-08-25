import random
print(r'''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
                     
''')
print(r'''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|           
''')
print(r'''
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \
|___/\___|_|___/___/\___/|_|  |___/
                                   
''')

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

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

#user's choice
if user_input == 0:
    print(rock)
elif user_input == 1:
    print(paper)
else:
    print(scissors)


computer_choice = random.randint(0, 2)

print("Computer's Chose: ")
#computer's choice
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

if user_input == 0 and computer_choice == 0 or user_input == 1 and computer_choice == 1 or user_input == 2 and computer_choice == 2:
    print("Its a draw.")
elif user_input == 0 and computer_choice == 1 or user_input == 1 and computer_choice == 2 or user_input == 2 and computer_choice == 0:
    print("You Lose")
else:
    print("You Win!")






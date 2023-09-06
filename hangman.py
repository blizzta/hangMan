word_list = ['luca', 'emilya', 'mario']
import random
word = random.choice(word_list)
display = []
finish_game = False
player_lives = 3

print('Hello do you want to play a round of hangman ??????\n')

for letter in word:
    display += '_'
#print(display)

while not finish_game :

 guess = input('Choose a letter ').lower()

 for position in range(len(word)):
   letter = word[position]
   
   if letter == guess:
       display[position] = letter
       
 if guess not in word:
        print(f'Your letter was not there, you still have {player_lives}life ')
        player_lives -= 1
        
 print(f"{''.join(display)}")

 if player_lives == 0:
     finish_game = True
     
     print('You didnt guess the word, unfortunately you lost')
 
 if '_' not in display:
     finish_game = True
     print('Congratulations you guessed the word')
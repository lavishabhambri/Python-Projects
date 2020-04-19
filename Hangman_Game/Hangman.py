#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
def hangman():
    word = random.choice(['hello','little','red','python','tiger','superman', 'love', 'play', 'save water','corona', 'animal', 'india'])
    valid_letters = 'abcdefghijklmnopqrstuvwxyz' #list of valid letters
    turns = 10        #total no. of turns to the user
    guess_made = ''
    while len(word)>0:   #when there is no word selected at all
        main = ""        #this word is generated randomly everytime
        misssed = 0      #how many has the user misssed
        
        for letter in word :
            if letter in guess_made:
                main =main +letter
            else:
                main = main+ '_' +" "
                
        if main == word:
            print(main)
            print('You win!')
            break
        print("Guess the word", main)
        guess = input()
        
        if guess in valid_letters :
            guess_made = guess_made + guess
        else:
            print('Enter a valid character')
            guess = input()
        
        if guess not in word :
            turns = turns-1
            if turns ==9:
                print('9 turns left')
                print(15*"* ")
            if turns ==8:
                print('8 turns left')
                print(15*"* ")
                print("     0      ")
            if turns ==7:
                print('7 turns left')
                print(15*"* ")
                print("     0      ")
                print("     |      ")
            if turns ==6:
                print('6 turns left')
                print(15*"* ")
                print("     0      ")
                print("     |      ")
                print("    /       ")
            if turns ==5:
                print('5 turns left')
                print(15*"* ")
                print("     0      ")
                print("     |      ")
                print("    / \      ")
            if turns ==4:
                print('4 turns left')
                print(15*"* ")
                print("    \0      ")                    
                print("     |      ")
                print("    / \      ")
            if turns == 3:
                print('3 turns left')
                print(15*"* ")
                print("   \ 0 /      ")
                print("     |      ")
                print("    / \      ")
            if turns == 2:
                print('2 turns left')
                print(15*"* ")
                print("   \ 0 /|      ")
                print("     |      ")
                print("    / \      ")
            if turns == 1:
                print('1 turns left')
                print('Last breaths counting, take care!')
                print(15*"* ")
                print("   \ 0_|/   ")
                print("     |      ")
                print("    / \      ")
            if turns == 0:
                print('You loose')
                print('You let a kind man die!')
                print(15*"* ")
                print("    0_|   ")
                print("   /|\      ")
                print("   / \      ")
                break
                
                
name = input('Enter your name')
print('Welcome! ',name)
print(20*'* ')
print('Try to guess the word in less than 10 try')

hangman()

print('')


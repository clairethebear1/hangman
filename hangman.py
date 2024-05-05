import random

print("Hello, and welcome to hangman!!")
print("-------------------------------------------------")

wordDictionary = ["word", "diamond", "claire", "ethan", "best", "dad", "mom", "summmer", "school", "boring", "joe", "coding"]

randomWord = random.choice(wordDictionary)
wrong = 0
for x in randomWord:
    print("_", end=" ")

def print_hangman(wrong):
    if wrong == 0:
        print(" _______     ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|_______   ")
    elif wrong == 1:
        print(" _______     ")
        print("|      |      ")
        print("|      O      ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|_______   ")
    elif wrong == 2:
        print(" _______     ")
        print("|      |      ")
        print("|      O      ")
        print("|      |      ")
        print("|              ")
        print("|              ")
        print("|_______   ")
    elif wrong == 3:
        print(" _______     ")
        print("|      |      ")
        print("|      O      ")
        print("|     /|      ")
        print("|              ")
        print("|              ")
        print("|_______   ")
    elif wrong == 4:
        print(" _______     ")
        print("|      |      ")
        print("|      O      ")
        print("|     /|\     ")
        print("|              ")
        print("|              ")
        print("|_______   ")
    elif wrong == 5:
        print(" _______     ")
        print("|      |      ")
        print("|      O      ")
        print("|     /|\     ")
        print("|     /       ")
        print("|              ")
        print("|_______   ")
    elif wrong == 6:
        print(" _______     ")
        print("|      |      ")
        print("|      O      ")
        print("|     /|\     ")
        print("|     / \     ")
        print("|              ")
        print("|_______   ")

def printWord(guessedLetters):
    counter = 0
    rightLetters = 0
    for char in randomWord:
        if char in guessedLetters:
            print(randomWord[counter], end=" ")
            rightLetters += 1
        else: 
            print("_", end=" ")
        counter += 1
    return rightLetters

def printLines():
    print("\r")
    for char in randomWord:
        print("\u203E", end=" ")

length_of_word_to_guess = len(randomWord)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while (amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess):
    print("\nLetters guesssed so far: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")
    
    letterGuessed = input("\nPlease guess a letter")
    ###User is right
    if(randomWord[current_guess_index] == letterGuessed):
        print_hangman(amount_of_times_wrong)
        ###Print word
        current_guess_index+=1
        current_letters_guessed.append(letterGuessed)
        current_letters_right = printWord(current_letters_guessed)
        printLines()
    ### User was wrong af
    else:
        amount_of_times_wrong +=1
        current_letters_guessed.append(letterGuessed)
        print_hangman(amount_of_times_wrong)
        ### Print word
        current_letters_right = printWord(current_letters_guessed)
        printLines()

print("Game is over! Thanks for playing :)")
print("Here is the word since you were too dumb to guess it:", randomWord)

    
















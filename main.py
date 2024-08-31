"""
game asks user for a name - then welcomes the user and ask if the user is ready to play

since strings have indexes there is not need for a list right -- i think

a word like [python] 

words are blank until user guesses the right letter so the has to be an underline of sort 

for each failed attempt the hangman icons starts to load until it is completely hanged 

for the hangman i will use the characters available 
"""

""" def hangman():
    print("-------")
    print("      |")
    print("      |")
    print("      O")
    print("     /|\\")
    print("     / \\")

print("NOTE -- ALL WORDS ARE IN LOWERCASE")
word1 = "python"
#word2 = "______"
print(word1)
#print(word2)

user_guess = input("guess a character in the hidden word: ")
if (user_guess in word1):
    if (len(user_guess) != 0):
        print("just a character needed")
    hangman()
else:
    print("wrong guess") """

from random import *

def hangman(hangman):
    graphic = [
        """
           +--------+
           |
           |
           |
           |
           |
           |
           +-----------
           +-----------
        """,
        """
           +--------+
           |        |
           |        O
           |
           |
           |
           |
           +-----------
           +-----------
        """,
        """
           +--------+
           |        |
           |        O
           |        |
           |
           |
           |
           +-----------
           +-----------
        """,
        """
           +--------+
           |        |
           |        O
           |       /|
           |
           |
           |
           +-----------
           +-----------
        """,
        """
           +--------+
           |        |
           |        O
           |       /|\\
           |
           |
           |
           +-----------
           +-----------
        """,
        """
           +--------+
           |        |
           |        O
           |       /|\\
           |       /
           |
           |
           +-----------
           +-----------
        """,
         """
           +--------+
           |        |
           |        O
           |       /|\\
           |       / \\
           |
           |
           +-----------
           +-----------
        """
    ]
    print(graphic[hangman])
    return

def start():
    print("Let's play a game of Hangman in your terminal")
    while game():
        pass

def game():
    dictionary = ["python", "linux", "mobile", "screen", "software"]
    word = choice(dictionary)
    word_length = len(word)
    clue = word_length * ['_']
    tries = 6
    letters_tried = ''
    guesses = 0
    letters_right = 0
    letters_wrong = 0

    while (letters_wrong != tries) and ("".join(clue) != word):
        letter = guess_letter()
        if len(letter) == 1 and letter.isalpha():
            if letters_tried.find(letter) != -1:
                print(f"You've already picked {letter}")
            else:
                letters_tried = letters_tried + letter
                first_index = word.find(letter)
                if first_index == -1:
                    letters_wrong += 1
                    print(f"Sorry, {letter} isn't what we're looking for.")
                else:
                    print(f"Congratulations!! {letter} is correct")
                    for i in range(word_length):
                        if letter == word[i]:
                           clue[i] = letter
        else:
            print("Choose another")
        
        hangman(letters_wrong)
        print("".join(clue))
        print(f"Guesses: {letters_tried}")

        if letters_wrong == tries:
            print("GAME OVER")
            print(f"THE WORD WAS: {word}")
            break
        if "".join(clue) == word:
            print("YOU WIN!!!")
            print(f"THE WORD WAS: {word}")
            break
    return play_again()
    

def guess_letter():
    print()
    letter = input("Guess the mystery word :)  ")
    letter.strip()
    letter.lower()
    print()
    return letter

def play_again():
    answer = input("Would you like to play again? y/n ")
    if answer in ("y", "Y", "yes", "Yes", "Of course!"):
        return answer
    else:
        print("Thank you very much for playing game. See you next time!")
    
if __name__ == '__main__':
   start()

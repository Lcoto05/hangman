import random
import hangman_words
import hangman_art


chosen_word = random.choice(hangman_words.word_list)

complete = False

lives = 6
#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

print(hangman_art.logo)

display = []
word_length = len(chosen_word)
for _ in range (word_length):
    display.append("_")
print(display)




while not complete:
    guess = input("Guess a letter: \n").lower()
    
    for i in range (word_length):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter
    if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                complete = True
                print("You lose.")
                print(f"The word was: {chosen_word}")
    print(f"{' '.join(display)}")

    if "_" not in display:
        complete = True
        print("You won!")
    print(hangman_art.stages[lives])



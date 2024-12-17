from termcolor import colored, cprint
import random



def pick_word():
    count = 0
    r = open('Words.txt', 'r')
    word_list = r.readline().split(", ")

    for x in word_list:
        if "-" in x:
            word_list.remove(x)

    word = random.choice(word_list)
    return word



def game(word):
    ui = "_" * len(word)

    cprint("Welcome to Hangman! The word is " + str(len(word)) + " letters long. you have 10 guesses. You may start: ", 'cyan')
    print(ui)
    lives = 10
    guess_list = []
    while "_" in ui and lives != 0:
        guess = input()

        if guess in word and guess not in guess_list:
            cprint("'" + guess.capitalize() + "'" + " is correct!", 'green')

            for x in range(len(word)):
                if word[x] == guess:
                    ui = ui[:x] + guess + ui[x + 1:]


            print(ui)
            guess_list += guess
        elif guess not in guess_list:
            cprint("'" + guess.capitalize() + "'" + " Not in word, try again", 'red')
            lives -= 1
            guess_list += guess
        else:
            cprint("'" + guess.capitalize() + "'" + " Already guessed, try another letter", 'yellow')


    if "_" not in ui:
        cprint("Congrats! The word was " + word + ". Would you like to play again? Y/N", 'magenta')
    else:
        cprint("Unlucky! The word was " + word + ". Would you like to play again? Y/N", 'magenta')





def main():

    while True:
        game(pick_word())
        restart = input()
        if restart == "Y" or restart == "y":
            continue
        else:
            return False



main()


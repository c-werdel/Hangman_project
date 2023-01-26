from urllib.request import urlopen
import random
import urllib.request

def read_words():
    with urllib.request.urlopen("http://norvig.com/ngrams/sowpods.txt") as response:
        myfile = response.read().decode('utf-8')
    return(myfile)

def get_word(myfile):
    word_list = myfile.split() 
    word_choice = random.choice(word_list) 
    return(word_choice)

def letter_checker(word_choice):
    print("Guess That Word")
    word_completion = "_" *len(word_choice) 
    word_choice = list(word_choice) 
    user_line = list(word_completion)
    wrong_guesses = []
    print("Your word is", user_line)
    
    while True:
        guess = input("Guess a letter ").upper() 
        index_count = 0
        for letter in word_choice:
            if letter == guess:
                print("Correct that letter is in the word")
                user_line[index_count] = guess
            index_count += 1
        print(user_line)

        if guess not in word_choice:
            print("Sorry that letter is not in the word")
            wrong_guesses.append(guess)
            print("Guessed letters: " , wrong_guesses)

if __name__ == "__main__":
    myfile = read_words()
    choice_word = get_word(myfile)
    play = letter_checker(choice_word)

    

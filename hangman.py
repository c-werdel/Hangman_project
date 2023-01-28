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
    fail_count = 0
    fail_limit = 12
    print("Guess That Word")
    word_completion = "_" *len(word_choice) 
    # word_choice = list(word_choice) 
    user_line = list(word_completion)
    wrong_guesses = []
    print("Your word is", user_line)
    playing = True

    while playing:
        print("Letters guessed wrong: " , wrong_guesses,) 
        print("You have used up", + fail_count, 'guess of', fail_limit, 'total guesses') 
        guess = input("Guess a letter ").upper()
        
        index_count = 0
        correct_printout = False
        for letter in word_choice:
            if letter == guess:
                correct_printout = True
                user_line[index_count] = guess
            index_count += 1
        if correct_printout:
            print("Correct", guess, "is in the word") 
        print(user_line)
        if fail_count >= 12:
            fail_count -= 1

        if guess not in word_choice: #only wrong guesses will contrbute to the fail count
            print("Sorry", guess,  "is not in the word")
            wrong_guesses.append(guess)
            fail_count += 1

        if user_line == word_choice: #if user line matches word_choice
            print("correct you guessed", user_line, "and the word was", word_choice,)

        if fail_count == fail_limit:
            print("Sorry you lost the word was" , word_choice)
        
    # new_game = input("Do you want to play again? Enter 'y' or 'n' ") #THIS IS A WORK IN PROGRESS SECTION

    # if new_game[0].lower()=='y':
    #     playing = True
    #     continue
    # else:
    #     print("Thanks for playing")
    #     break

if __name__ == "__main__":
    myfile = read_words()
    choice_word = get_word(myfile)
    letter_checker(choice_word)

    

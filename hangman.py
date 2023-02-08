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
    guessed = []
    print(word_choice)
        
    while True:
        print("Your word is", user_line)
        print("Letters guessed wrong: " , guessed,) 
        print("You have used up", + fail_count, 'guess of', fail_limit, 'total guesses') 
        guess = input("Guess a letter ").upper()
        
        if guess in guessed or guess in user_line:
            print("you already guessed", guess)
            continue
        #

        index_count = 0
        correct_printout = False
        for letter in word_choice:
            if letter == guess:
                correct_printout = True
                user_line[index_count] = guess
            index_count += 1
        if correct_printout:
            print("Correct", guess, "is in the word")
            if fail_count > 0:
                fail_count -= 1 

       
        if guess not in word_choice: #only wrong guesses will contrbute to the fail count
            print("Sorry", guess,  "is not in the word")
            guessed.append(guess)
            fail_count += 1
    
        if "".join(user_line) == word_choice: #if user line matches word_choice
            print("correct you guessed", user_line, "and the word was", word_choice,)
            break
        #put a list back into a string
        
        if fail_count >= fail_limit:
            print("Sorry you lost the word was" , word_choice)
            break

    answer = input("Do you want to play again? Y/N ")

    if answer.lower() == "y" or answer.lower() == "yes":
       game_setup()
    else:
        print("Goodbye!")

def game_setup():
    choice_word = get_word(myfile)
    letter_checker(choice_word)

if __name__ == "__main__":
    myfile = read_words()
    game_setup()
  

    

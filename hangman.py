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

if __name__ == "__main__":
    myfile = read_words()
    choice_word = get_word(myfile)
    print(choice_word)
    

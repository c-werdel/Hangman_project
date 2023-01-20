from urllib.request import urlopen
import random
import urllib.request

def read_words():
    with urllib.request.urlopen("http://norvig.com/ngrams/sowpods.txt") as response:
        myfile = response.read().decode('utf-8')
    # print(myfile) #for testing
    return(myfile)

def get_word(myfile): #myfile is plugged in as an input
    word_list = myfile.split() #The str.split() method splits the string into a list of substrings
    word_choice = random.choice(word_list) #word_choice = the word that will be guessed by the user
    print(word_choice)

if __name__ == "__main__":
#     read_file = read_words()
# #  print(read_file)
    myfile = read_words()
    get_word(myfile)    
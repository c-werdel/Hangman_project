from urllib.request import urlopen

def read_word():
    link = "http://norvig.com/ngrams/sowpods.txt"
    f = urlopen(link)
    myfile = f.read()
    print(myfile)
    
# def get_word():
#     pass

# def guess_letter():
#     pass

if __name__ == "__main__":
 read_file = read_word()
 print(read_file)
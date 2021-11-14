def countWord(bookWords): #Count the repetition of words
    dictionary = {}
    dictionary2 = {}
    splitWords = bookWords.lower()
    splitWords = splitWords.split()
    for word in splitWords: #Adds value to the word
        dictionary[word] = dictionary.get(word, 0) + 1

    for word in dictionary.keys():
        x = word #get the key
        y = dictionary.get(x) #get the key's value
        if y>1:  #Checks if value is more than one
            # print(x,y)
            dictionary2[x]=y #Adds in word with value above 2 on new dictionary
    return dictionary2 #returns the value of a new dictionary


def start(): #Run the program
    bookFile = open("book.txt", "r")
    content = bookFile.read()
    mainDictionary = countWord(content)

    print(mainDictionary) #Prints the key-value pair of dictionary2(new dictionary)

start()


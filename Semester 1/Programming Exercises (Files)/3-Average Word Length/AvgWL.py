#Numbers Initial Value
averageWordLength = 0
sumOfLengthOfWordTokens = 0
numberOfWordTokens = 0

bookFile = open("book.txt", "r")
content = bookFile.read()
splitWords=content.split() #Creates a list composed of splitted words as the items

for x in splitWords: #For every item in the list,
    numberOfWordTokens +=1 #Adds the variable value by 1
    sumOfLengthOfWordTokens += len(x) #Adds the variable value by the length of the item

#Calculates the average word length by dividing the sum of all the lengths of word tokens with number of word tokens
averageWordLength=sumOfLengthOfWordTokens/numberOfWordTokens

#Prints the average word length along with other number values
print("Average Word Length: ",averageWordLength )
print("\nSum of All Lengths of Word Tokens: ",sumOfLengthOfWordTokens)
print("Number of Word Tokens: ",numberOfWordTokens)
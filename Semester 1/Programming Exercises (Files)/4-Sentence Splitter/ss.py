#A pair of list to convert special exceptions from and to back and forth
shortTitles = ["Mr.", "Mrs.", "Dr.","Jr."]
longTitles = ["Mister", "Missus", "Doctor","JR"]
shortInternal = ["e.g.", "i.e."]
longInternal = ["EG", "IE"]

shortText=input("Enter a short text: ") #Asks the user to input the short text

for x in shortTitles: #Replaces titles with another name to prevent periods replacement
     i = shortTitles.index(x)
     shortText = shortText.replace(x, longTitles[i])
for x in shortInternal: #Replaces periods internal with another name to prevent periods replacement
     i = shortInternal.index(x)
     shortText = shortText.replace(x, longInternal[i])

shortText = shortText.replace(". ", ".\n") #Replaces period with a period and new line
shortText = shortText.replace("? ", "?\n") #Replaces question mark with a question mark and new line
shortText = shortText.replace("! ", "!\n")  #Replaces exclamation mark with an exclamation mark and new line

for x in longTitles: #Reverts  new title name back to old name
    i = longTitles.index(x)
    shortText = shortText.replace(x, shortTitles[i])
for x in longInternal: #Reverts new internal name back to old name
    i = longInternal.index(x)
    shortText = shortText.replace(x, shortInternal[i])

file = open("result.txt", "w")
file.write(shortText) #Write the modified short text
file.close()



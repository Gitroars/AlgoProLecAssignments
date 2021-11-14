oldFile = open("oldFile.txt","r")
oldContent = oldFile.readlines() #Each line of oldFile becomes a member of the list
newFile = open("newFile.txt","w")
i = 1 #numbering starts at number 1
for line in oldContent: #At every list(line),
 newFile.write(f"{i} "+line) #Write the value of i(for numbering) before the line sentence
 i+=1 #Afterwards, increase the value of i by 1




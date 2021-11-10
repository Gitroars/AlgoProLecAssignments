oldFile = open("oldFile.txt","r")
oldContent = oldFile.readlines()
print(oldContent)
newFile = open("newFile.txt","w")
i = 1
for line in oldContent:
 newFile.write(f"{i} "+line)
 i+=1




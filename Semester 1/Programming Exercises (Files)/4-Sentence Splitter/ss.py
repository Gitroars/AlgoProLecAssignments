
defaultInput="Mr. Miyagi bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't."
# fileContent=input("Enter the file's content: ")

defaultInput=defaultInput.replace(". ",".\n ")
defaultInput=defaultInput.replace("?","?\n ")
defaultInput=defaultInput.replace("!","!\n ")
file=open("result.txt","w")
file.write(defaultInput)
file.close()

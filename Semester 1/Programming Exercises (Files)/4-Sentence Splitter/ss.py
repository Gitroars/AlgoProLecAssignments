shortTitles = ["Mr.", "Mrs.", "Dr."]
longTitles = ["Mister", "Missus", "Doctor"]
shortInternal = ["e.g.", "i.e."]
longInternal = ["EG", "IE"]



defaultInput = "Mr. Miyagi bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't."




for x in shortTitles:
     i = shortTitles.index(x)
     defaultInput = defaultInput.replace(x, longTitles[i])
for x in shortInternal:
     i = shortInternal.index(x)
     defaultInput = defaultInput.replace(x,longInternal[i])

defaultInput = defaultInput.replace(". ", ".\n")
defaultInput = defaultInput.replace("?", "?\n")
defaultInput = defaultInput.replace("!", "!\n")

for x in longTitles:
    i = longTitles.index(x)
    defaultInput = defaultInput.replace(x, shortTitles[i])
for x in longInternal:
    i = longInternal.index(x)
    defaultInput = defaultInput.replace(x, shortInternal[i])

file = open("result.txt", "w")
file.write(defaultInput)
file.close()



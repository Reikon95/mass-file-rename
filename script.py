import os, os.path
import re


# input dir here:

dir = ""

# add phrase to remove from here

singlePhraseToRemove = re.compile()

# what to replace with: 

replaceWith = ''

targetedFiles = os.listdir(dir)

print('number of files to rename:', len(targetedFiles))

for file in targetedFiles:
    print(file)
    new_name = re.sub(singlePhraseToRemove, replaceWith, file)
    os.rename(dir + "/" + file, dir + "/" + new_name)

print(targetedFiles)    


#Import library
import json
# This is a python library for 'Text Processing Serveices', as the offcial site suggests.
import difflib
from difflib import SequenceMatcher

#Let's load the same data again
data = json.load(open("data.json"))

#Run a Sequence Matcher
#First parameter is 'Junk' which includes white spaces, blank lines and so onself.
#Second and third parameters are the words you want to find similarities in-between.
#Ration is used to find how close those two words are in terms of number
value = SequenceMatcher(None, "rainn", "rain").ratio()

#Print out the value
print(value)

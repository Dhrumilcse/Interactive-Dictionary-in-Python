#Import library
import json
# This is a python library for 'Text Processing Serveices', as the offcial site suggests.
import difflib
from difflib import get_close_matches

#Let's load the same data again
data = json.load(open("data.json"))

#Before you dive in, the basic template of this function is as follows
#get_close_matches(word, posibilities, n=3, cutoff=0.66)
#First parameter is of course the word for which you want to find close matches
#Second is a list of sequences against which to match the word
#[optional]Third is maximum number of close matches
#[optional]where to stop considering a word as a match (0.99 being the closest to word while 0.0 being otherwise)

output = get_close_matches("rain", ["help","mate","rainy"], n=1, cutoff = 0.75)

# Print out output, any guesses?
print(output)

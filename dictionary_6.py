#Import library
import json
from difflib import get_close_matches

#Loading the json data as python dictionary
#Try typing "type(data)" in terminal after executing first two line of this snippet
data = json.load(open("data.json"))

#Function for retriving definition
def retrive_definition(word):
    #Removing the case-sensitivity from the program
    #For example 'Rain' and 'rain' will give same output
    #Converting all letters to lower because out data is in that format
    word = word.lower()

    #Check for non existing words
    #1st elif: To make sure the program return the definition of words that start with a capital letter (e.g. Delhi, Texas)
    #2nd elif: To make sure the program return the definition of acronyms (e.g. USA, NATO)
    #3rd elif: To find a similar word
    #-- len > 0 because we can print only when the word has 1 or more close matches
    #-- In the return statement, the last [0] represents the first element from the list of close matches
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input("Did you mean %s instead? [y or n]: " % get_close_matches(word, data.keys())[0])
        #-- If the answers is yes, retrive definition of suggested word
        if (action == "y"):
            return data[get_close_matches(word, data.keys())[0]]
        elif (action == "n"):
            return ("The word doesn't exist, yet.")
        else:
            return ("We don't understand your entry. Apologies.")

#Input from user
word_user = input("Enter a word: ")

#Retrive the definition using function and print the result
print(retrive_definition(word_user))

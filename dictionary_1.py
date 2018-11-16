#Import library
import json

#Loading the json data as python dictionary
#Try typing "type(data)" in terminal after executing first two line of this snippet
data = json.load(open("data.json"))

#Function for retriving definition
def retrive_definition(word):
    return data[word]

#Input from user
word_user = input("Enter a word: ")

#Retrive the definition using function and print the result
print(retrive_definition(word_user))

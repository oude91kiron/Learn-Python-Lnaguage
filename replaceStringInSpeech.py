# Write code for the function play_game, which takes in as inputs parts_of_speech
# (a list of acceptable replacement words) and ml_string (a string that 
# can contain replacement words that are found in parts_of_speech). Your play_game
# function should return the joined list replaced, which will have the same structure
# as ml_string, only that replacement words are swapped out with "person", since this
# program cannot replace those words with user input. 

parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

ml_string = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""

def word_in_pos(word, parts_of_speech): # take word and array of parts of speech
    for pos in parts_of_speech:  # for every element in the array parts_of_speech
        if pos in word: # if the element from the array part of the word
            return pos  # return that element "PLACE, PERSON, PLURALNOUN or NOUN"
    return None # or return None
        
def play_game(ml_string, parts_of_speech):    # Take String as a speech and arrary of parts of speech 
    replaced = [] # define empty array
    # your code here
    ml_string = ml_string.split() # switch the String to an array
    for word in ml_string : # for every element in the array
        replacement = word_in_pos(word, parts_of_speech) # check if the word part of speech
        if replacement != None : # if the word part of speech 
            word = word.replace(replacement, "dog") # switch the replacemet value by string "dog" 
            replaced.append(word) # add the word to the replaced array
        else:
            replaced.append(word) # else add the word to the replaced array
    replaced = " ".join(replaced) # switch the array to string
    return replaced # return that string 
    
print "Before excute the program:"
print ml_string
print " "
print "After excute the program:"
print play_game(ml_string, parts_of_speech)       

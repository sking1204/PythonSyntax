#For a list of words, print out each word on a separate line, but in all uppercase.
# How can you change a word to uppercase? Ask Python for help
# on what you can do with strings!

# str=['cat','dog','mouse','goat','bear' ]

# for word in str:
#     print(word.upper()) 


#Turn that into a function, print_upper_words. Test it out.
# (Don’t forget to add a docstring to your function!

# def print_upper_words(str):
#     for word in str:
#         print(word.upper())







#Change that function so that it only prints words that start
# with the letter ‘e’ (either upper or lowercase).

def print_upper_words(strlist):

    for word in strlist:

        if word.startswith("E") or word.startswith("e"):
            print(word.upper())









#Question for mentor: 
#How can I make the function below include both cases of a letter (upper and lower)


#Make your function more general: you should be able to pass 
#in a set of letters, and it only prints words that start with one of those letters.

## this should print "HELLO", "HEY", "YO", and "YES"

#print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   #must_start_with={"h", "y"})



def print_upper_words_2(strlist,startletter):
    

    for word in strlist:

        for letter in startletter:
            if word.startswith(letter):
                print(word.upper())
         


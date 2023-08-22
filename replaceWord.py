
# method to replace word
def replace_word():

    #base string
    str = "Hi guys, I am Peter, and hi hi hi hi hi"

    # set string to lower case
    str = str.lower()

    #print string
    print(str)

    #set variables
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")

    #set variables to lower case
    word_replacement = word_replacement.lower()
    word_to_replace = word_to_replace.lower()

    #print with replacement
    print(str.replace(word_to_replace, word_replacement))

#run method
replace_word()
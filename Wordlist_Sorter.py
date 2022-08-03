#This script is a simple sorting on utf-8 encoded wordlists.
#The sorting is based on the rule of minimum requirements of 8 characters,
# comprising at least 3 of the 4 types of characters (upper case, lower case, number and special character).


#It open the file you want to sort and create another one where to get the filtered content (you can specify an other encoding).
with open("Existing_Wordlist.txt",'r', encoding = "utf-8") as file, open("Sorted_Wordlist.txt",'w') as new_file:

    text = file.read()
    list = text.split("\n")


    #Testing for the presence of the different types of characters.
    for word in list:

        #Declaring bool variables NB (NumBer), UC (UpperCase), LC (LowerCase) and SC (Special Character).
        NB = False
        UC = False
        LC = False
        SC = False

        if any(map(str.isdigit, word)):
            NB = True

        if any(map(str.isupper, word)):
            UC = True

        if any(map(str.islower, word)):
            LC = True

        SC = bool(set(""" &é"'(-è_çà)=^$*ù!:;,~#[|`\^@]}{¤°+¨£µ%§/.?<>""").intersection(word))


        if len(word) >= 8:

            if LC and UC and NB or \
            UC and NB and SC or \
            NB and SC and LC or \
            SC and LC and UC:
                
                #If the word matches the requirements, it will be written to: "Sorted_Wordlist.txt".
                new_file.write(word + "\n")
                #Be careful with the last "\n" wich creates a new line at the end of the file.
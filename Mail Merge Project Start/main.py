#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Names/invited_names.txt", "r") as file:
    namelist = file.readlines()


for names in namelist:
    with open("Input/Letters/starting_letter.txt", "r") as file:
        txt = file.read()
    names = str(names)
    names = names.strip("\n")
    txt = txt.replace("[name]", names)
    with open(f"Output/ReadyToSend/letter_for_{names}", "w") as file:
        file.write(txt)

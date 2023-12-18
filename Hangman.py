file = open('Hangman.txt')  
content = file.readlines()

word = content[int(input("Wählen Sie ein Wort. \n Dazu geben Sie bitte eine Zahl von 1-120 aus: ")) - 1].strip().lower()
my_set_word = set(word)
wrong_letters = []

the_answere = []
my_set_input = set(the_answere)
wrong = []

while(my_set_input != my_set_word):    
    eingabe = str(input("Bitte geben Sie ein Buchstaben ein: ")).lower()

    if eingabe == word:
        break
    else:   
        if eingabe in word:
            the_answere.append(eingabe)
        else:
            wrong.append("X")
            wrong_letters.append(eingabe)     

    my_set_input = set(the_answere)
    
    progress = ''.join([char if char in the_answere else '_' for char in word])
    
    print(f"\n {wrong} \n FALSCHE BUCHSTABEN:{wrong_letters}")
    print(f"Fortschritt: {progress}\n")

    #print(f"Word: {my_set_word.intersection(my_set_input)}")
    
print(f"Herzlichen Glückwunsch, das Wort war: {word} \n Noch eine Runde?")
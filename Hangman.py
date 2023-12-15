file = open('Hangman.txt')  
content = file.readlines()

word = content[int(input("Wählen Sie ein Wort. \n Dazu geben Sie bitte eine Zahl von 1-126 aus: ")) - 1].strip().lower()
my_set_word = set(word)

the_answere = []
my_set_input = set(the_answere)
wrong = []

while(my_set_input != my_set_word):    
    eingabe = str(input("Bitte geben Sie ein Buchstaben ein: ")).lower()
    
    if eingabe in word:
        the_answere.append(eingabe)
    else:
        wrong.append("X")
        print(wrong)

    my_set_input = set(the_answere)
    
    progress = ''.join([char if char in the_answere else '_' for char in word])

    print(f"Fortschritt: {progress}\n")
    
print(f"Herzlichen Glückwunsch, das Wort war: {word}")
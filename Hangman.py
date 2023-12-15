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
    
    progress = ''#.join([char if char in the_answere else '_' for char in word])
    
    for char in word:
        if char in the_answere:
           progress += char
        else:
            progress += '_'
    print(f"Fortschritt: {progress}\n")

    #print(f"Word: {my_set_word.intersection(my_set_input)}")
    
print(f"Herzlichen Glückwunsch, das Wort war: {word}")


'''
for char in word: Iteriert durch jeden Buchstaben im zu erratenden Wort (word).
char if char in the_answer else '_': Überprüft, ob der aktuelle Buchstabe (char) bereits vom Benutzer erraten wurde (char in the_answer). Wenn ja, wird der Buchstabe beibehalten, andernfalls wird ein Unterstrich ('_') verwendet, um den Buchstaben zu verdecken.
[...]: Diese Konstruktion erstellt eine Liste mit den Ergebnissen aus dem vorherigen Schritt für jeden Buchstaben im Wort.
Das Ergebnis ist eine Liste von Buchstaben und Unterstrichen, wobei die Buchstaben, die der Benutzer bereits erraten hat, unverändert bleiben und die noch nicht geratenen Buchstaben durch Unterstriche ersetzt werden.

''.join(...): Verbindet die Elemente der Liste zu einer Zeichenkette, wobei die Elemente durch nichts ('') getrennt werden. Dies erzeugt den Fortschritt des Hangman-Spiels als Zeichenkette.
Die Variable display_progress enthält also eine Zeichenkette, die den aktuellen Fortschritt des Spiels repräsentiert, wobei geratene Buchstaben sichtbar sind und noch nicht geratene Buchstaben durch Unterstriche ersetzt werden. Diese Zeichenkette wird dann in der nächsten Zeile ausgegeben, um dem Benutzer den aktuellen Fortschritt anzuzeigen.
'''
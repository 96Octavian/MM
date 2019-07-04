def legginomi():
    try:
        f = open("anagrafici.csv", "w")
    except FileNotFoundError:
        print("File non trovato")
        return
    input_string = "s"
    while input_string == "s":
        stringa = ""
        stringa += input("Nome? ")
        stringa += input("Cognome? ")
        stringa += input("Data? ")
        stringa += input("Luogo? ")
        f.write(stringa + "\n")
        input_string = input("Vuoi inserire un'altra persona? [s/n]")
    f.close()


def stampanomi():
    try:
        f = open("anagrafici.csv", "r")
    except FileNotFoundError:
        print("File non trovato")
        return
    for line  in f:
        line = line.split(";")
        print(f'Nome: {line[0]}, Cognome: {line[1]}, Data: {line[2]}, Luogo: {line[3]}' )


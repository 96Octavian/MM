def legginomi():
    try:
        f = open("anagrafici.csv", "w")
        input_string = "s"
        while input_string == "s":
            stringa = ""
            stringa += input("Nome? ") + ";"
            stringa += input("Cognome? ") + ";"
            stringa += input("Data? ") + ";"
            stringa += input("Luogo? ") + ";"
            f.write(stringa + "\n")
            input_string = input("Vuoi inserire un'altra persona? [s/n]").lower()
        f.close()
    except FileNotFoundError:
        print("File non trovato")


def stampanomi():
    try:
        f = open("anagrafici.csv", "r")
        for line in f:
            line = line.split(";")
            print(f'Nome: {line[0]}, Cognome: {line[1]}, Data: {line[2]}, Luogo: {line[3]}')
    except FileNotFoundError:
        print("File non trovato")
        return


if __name__ == '__main__':
    """
    Imposta una funzione che stampi i campi contenuti nel file 'anagrafici.csv' e una che invece chieda l'inserimento
    di tali campi e li scrivanel file
    """
    print('Nel file sono presenti questi nomi:')
    print(stampanomi())
    print(f'Inserisci nuovi nomi')
    legginomi()
    print('File aggiornato')
    print(stampanomi())

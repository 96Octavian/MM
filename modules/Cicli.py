def letterainriga(nomefile, lettera):
    try:
        f = open("../files/" + nomefile, "r")
        lista = []
        a = 0
        for riga in f:
            a = 0
            for carattere in riga:
                if lettera == carattere:
                    a = a + 1
            lista.append(a)
        f.close()
        return lista
    except FileNotFoundError:
        print("File non trovato")


if __name__ == '__main__':
    """
    Definisci una funzione che ritorni le occorrenze di una lettera in ogni riga
    """
    print(f'Trovate: {letterainriga("parole.txt", "d")}')

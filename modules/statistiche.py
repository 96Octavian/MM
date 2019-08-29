def contaparola(stringa):
    a = stringa.split(" ")
    massimo = ""
    for i in a:
        if len(i) > len(massimo):
            massimo = i
    return massimo


def stampagrafico(listaparola):
    a = 1
    for i in listaparola:
        print(f'[riga {a}] {len(i) * "*"}')
        a += 1


def main(nomefile):
    f = open(nomefile, "r")
    lista = []
    for i in f:
        lista.append(contaparola(i))

    lista = list(map(contaparola, lista))
    stampagrafico(lista)


if __name__ == '__main__':
    """
    Trova per ogni riga la parola più lunga e stampa in un grafico la lunghezza
    """
    main("../files/" + "parole.txt")
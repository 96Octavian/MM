def ultima_parola(nome_file):
    try:
        f = open(nome_file, "r")
        ultime_parole = []
        lista = []
        for i in f:
            lista.append(i)
        a = map(parola,lista)
        a = map(lunghezza, a)
        return a
    except FileNotFoundError:
        print(f'Could not find file {nome_file}')



def parola(riga):
    parola = riga.split(" ")
    return parola[-1]

def lunghezza(parola):
    a = 0
    for i in parola:
        a = a + 1
    return a


if __name__ == "__main__":
    """
    Costruisci una lista con la lunghezza delle ultime parole di ogni riga nel file
    """
    print(f'Le lunghezze dell\'ultima parola di ogni riga sono {ultima_parola("../files/" + "parole.txt")}')

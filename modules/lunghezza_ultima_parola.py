def ultima_parola(nome_file):
    try:
        f = open(nome_file, "r")
        ultime_parole = []
        for line in f:
            ultime_parole.append(line.split(" ")[-1])
        lunghezza = [len(x) for x in ultime_parole]
        return lunghezza
    except FileNotFoundError:
        print(f'Could not find file {nome_file}')

if __name__ == "__main__":
    """
    Costruisci una lista con la lunghezza delle ultime parole di ogni riga nel file
    """
    print(f'Le lunghezze dell\'ultima parola di ogni riga sono {ultima_parola("parole.txt")}')

def ultima_parola(nome_file):
    f = open(nome_file, "r")
    ultime_parole = []
    for line in f:
        ultime_parole.append(line.split(" ")[-1])
    lunghezza = [len(x) for x in ultime_parole]
    print(lunghezza)

if __name__ == "__main__":
    ultima_parola('parole.txt')

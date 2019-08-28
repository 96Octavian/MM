def unica(filename, nomefile):
    try:
        f = open("../files/prestito.csv", "r")
        output = open("../files/" + filename, "w")
        output2 = open("../files/" + nomefile, "w")
        lista = []
        lista2 = []
        for line in f:
            if " " not in line:
                lista.append(line)
            else:
                lista2.append(line)
        for elem in lista:
            riga = elem.split(";")
            somma = int(riga[2])
            somma = somma + (somma * 10 / 100)
            riga[2] = str(int(somma))
            output.write(";".join(riga) + '\n')
        for elem in lista2:
            riga = elem.split(";")
            somma = int(riga[2])
            somma = somma + (somma * 20 / 100)
            riga[2] = str(int(somma))
            output2.write(";".join(riga) + '\n')
        f.close()
        output.close()
        output2.close()
    except FileNotFoundError:
        print("Could not find 'prestito.csv'")
    except FileExistsError:
        print(f'Could not create {filename}: file exists')


def nome_singolo(filename):
    try:
        f = open("prestito.csv", "r")
        output = open(filename, "w")
        lista = []
        for line in f:
            if " " not in line:
                lista.append(line)
        for elem in lista:
            riga = elem.split(";")
            somma = int(riga[2])
            somma = somma + (somma * 10 / 100)
            riga[2] = str(int(somma))
            output.write(";".join(riga) + '\n')
        f.close()
        output.close()
    except FileNotFoundError:
        print("Could not find 'prestito.csv'")
    except FileExistsError:
        print(f'Could not create {filename}: file exists')


def nome_doppio(filename):
    try:
        f = open("prestito.csv", "r")
        output = open(filename, "w")
        lista = []
        for line in f:
            if " " in line:
                lista.append(line)
        for elem in lista:
            riga = elem.split(";")
            somma = int(riga[2])
            somma = somma + (somma * 20 / 100)
            riga[2] = str(int(somma))
            output.write(";".join(riga) + '\n')
        f.close()
        output.close()
    except FileNotFoundError:
        print("Could not find 'prestito.csv'")
    except FileExistsError:
        print(f'Could not create {filename}: file exists')


if __name__ == '__main__':
    """
    Apri il file 'prestito.csv' e dividi le righe a seconda che abbiano solo un nome o anche un secondo nome.
    Scrivi quelli con un solo nome in un secondo file con la cifra aumentata del 10% e quelli con il secondo nome con
    la cifra aumentata del 20% in un terzo file
    """
    nome_singolo("nome_singolo.csv")
    nome_doppio("nome_doppio.csv")

if __name__ == '__main__':
    """
    Apri il file 'prestito.csv' e dividi le righe a seconda che abbiano solo un nome o anche un secondo nome.
    Scrivi quelli con un solo nome in un secondo file con la cifra aumentata del 10% e quelli con il secondo nome con
    la cifra aumentata del 20% in un terzo file
    """
    nome_singolo("nome_singolo.csv")
    nome_doppio("nome_doppio.csv")
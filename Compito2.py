def conta_parole(filename):
    try:
        f = open(filename, "r")
        o = open("output.txt", "w")
    except FileNotFoundError:
        return 0
    except:
        print("Non so che errore ci sia stato")
        return 0
        # Qualunque
    p = 0
    try:
        c = f.readline()
        while c:
            l = c.split(" ")
            p = p + len(l)
            c = f.readline()
    except IOError:
        print ("ERRORE")
        o.close()
        f.close()
    try:
        o.write(p)
    except IOError:
        print ("ERRORE")
        f.close()
        o.close()
    except TypeError:
        print("write() accetta solo stringhe")
        o.write(str(p))
    o.close()
    f.close()
    return p


def chiedi_nome():
    filename = input("Che file devo aprire? ")
    conta_parole(filename)


if __name__ == '__main__':
    chiedi_nome()
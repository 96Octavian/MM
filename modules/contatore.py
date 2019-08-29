def conta_parole(filename):
    try:
        f = open("../files/" + filename, "r")
        o = open("../files/output.txt", "w")
        p = 0
        c = f.readline()
        while c:
            l = c.split(" ")
            p = p + len(l)
            c = f.readline()
        o.write(str(p))
        return p
    except FileNotFoundError:
        print("Could not find file")
        return None
    except IOError:
        print("Write error")
    except:
        print("Non so che errore ci sia stato")
        return None
    finally:
        if 'o' in locals():
            o.close()
        if 'f' in locals():
            f.close()


def chiedi_nome():
    filename = input("Che file devo aprire? ")
    return conta_parole(filename)


if __name__ == '__main__':
    numero_parole = chiedi_nome()
    if numero_parole:
        print(f'Nel file ci sono {numero_parole} parole')

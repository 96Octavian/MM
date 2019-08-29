def unisciliste(lista1, lista2):
    lista = []
    for i in lista1:
        for a in lista2:
            if i == a:
                lista.append(a)
    return lista


def main(nomefile):
    lista = []
    f = open(nomefile, "r")
    for i in f:
        a = i.split(";")
        if int(a[1]) > 500:
            lista.append(a[0])
    return lista


def main2 (nomefile):
    f = open(nomefile, "r")
    lista = []
    for i in f:
        lista.append(i)
    lista = filter(nomefunzione, lista)
    return lista


def nomefunzione(elemento):
    a = elemento.split(";")
    return int(a[1]) > 500
















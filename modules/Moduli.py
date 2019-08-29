import numeri
from primo_o_secondo_nome import unica


def massimoimporto(file1, file2):
    unica(file1, file2)

    lista = []

    f = open(file1, "r")

    for i in f:
        lista.append(i.rstrip().split(";")[2])
    max_singol = numeri.massimo(lista)

    f = open(file2, "r")
    max_doppi = 0
    lista = []
    for i in f:
        lista.append(int(i.rstrip().split(";")[2]))
    for i in lista:
        if i > max_doppi:
            max_doppi = i
    return max_singol, max_doppi


if __name__ == '__main__':
    """
    Definisci una funzione che usando primo_o_secondo_nome.py e numeri.py restituisca l'importo massimo per entrambi
    i file
    """
    max_singolo, max_doppio = massimoimporto("../files/" + "nomefile", "../files/" + "altronomefile")
    print(f'Per i nomi sigoli il massimo è {max_singolo}, per i nomi doppi è {max_doppio}')

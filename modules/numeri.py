def ordine_decrescente(lista):
    ordinata = []
    while len(lista):
        massim = massimo(lista)
        ordinata.append(massim)
        lista = [x for x in lista if x != massim]
    return ordinata


def inversa(lista):
    nuova_lista = []

    for i in range(1, len(lista) + 1):
        nuova_lista.append(lista[len(lista) - i])
    return nuova_lista


def somma(lista):
    somma = 0
    for num in lista:
        somma = somma + num
    return somma


def massimo(lista):
    lista = list(map(int, lista))
    n_max = lista[0]
    for num in lista:
        if num > n_max:
            n_max = num
    return n_max


def numero():
    """Elabora l'input"""
    numeri = input("Inserisci una serie di numeri separati da spazi:\n")
    numeri = numeri.split()
    numeri = list(map(int, numeri))
    print(
        f'Massimo: {massimo(numeri)}, somma: {somma(numeri)}, inversa: {inversa(numeri)}, ordinata: {ordine_decrescente(numeri)}')


if __name__ == '__main__':
    """Chiedi all'utente una lista di numeri separati da spazio, e stampa a schermo il massimo, la somma,
    la lista inversa, la lista ordinata in ordine crescente
    Argomenti: funzioni con parametri, cicli
    Input: "4 7 23"
    Output: Max: 23, somma: 34, inversa: 23 7 4, ordinata: 4 7 23
    Hint: tante funzioni"""
    numero()

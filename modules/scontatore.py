def sconta_da_fighi(prezzi, sconto):
    return [x - (x * sconto / 100) for x in prezzi]


def scontati(prezzi, sconto):
    scontati = []
    for prezzo in prezzi:
        prezzo -= prezzo * sconto / 100
        scontati.append(prezzo)
    return scontati


def sconto(prezzo_iniziale):
    prezzo_iniziale = int(prezzo_iniziale)
    if prezzo_iniziale > 50:
        mult = 20
    else:
        mult = 10
    return prezzo_iniziale * mult / 100


def stampa_sconto(nome_file):
    """Calcola e stampa il risultato"""
    try:
        f = open("../files/" + nome_file, "r")
        for line in f:
            try:
                prodotto, prezzo = line.split(";")
                prezzo = int(prezzo)
                differenza = sconto(prezzo)
                print(f'{prodotto}: {prezzo} - {differenza} = {prezzo - differenza}')
            except ValueError:
                print('Wrong line format')
    except FileNotFoundError:
        print("File not found")
    return


if __name__ == '__main__':
    """Dato un file contenente per ogni riga nome del prodotto e prezzo, stampa a video il prezzo iniziale, lo sconto
    e il prezzo finale. Lo sconto è del 10% se costa meno di 50, altrimenti del 20%.
    Argomenti: Gestione eccezioni, almeno due funzioni con parametri
    Input: "Maglietta;20"
    Output: "Maglietta: 20 - 2 = 18"
    Hint: funzione sconto(prezzo) ritorna lo sconto"""

    stampa_sconto('prodotti.csv')

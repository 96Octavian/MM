def sconta_da_fighi(prezzi, sconto):
    return [x - (x * sconto / 100) for x in prezzi]


def sconta(prezzi, sconto):
    scontati = []
    for prezzo in prezzi:
        prezzo -= prezzo * sconto / 100
        scontati.append(prezzo)
    return scontati

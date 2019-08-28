def seleziona_con_for(lista):
    divisori = []
    for i in lista:
        if i%2==0:
            if i%3 ==0:
                divisori.append(i)
    return divisori


def filtro(n):
    return n %2 == 0 and n % 3 == 0


def seleziona_con_filter(lista):
    return list(filter(filtro, lista))


if __name__ == '__main__':
    """
    Partendo da una lista di numeri restituisci i numeri divisibili sia per 2 che per 3
    """
    print(f'[filter] {seleziona_con_filter([6, 18, 11, 123123, 2, 35433])} sono divisibili per 2 e per 3')
    print(f'[ciclo for] {seleziona_con_for([6, 18, 11, 123123, 2, 35433])} sono divisibili per 2 e per 3')

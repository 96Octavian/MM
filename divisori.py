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
    return filter(filtro, lista)


if __name__ == '__main__':
    seleziona_con_filter([6, 18, 11, 123123, 2, 35433])

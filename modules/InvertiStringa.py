def InvertiStringa():
    stringa = input("Inserisci una stringa: ")
    inversa = ''
    index = len(stringa) - 1

    while(index>=0):
        inversa += stringa[index]
        index -= 1

    return inversa


if __name__ == '__main__':
    """
    Chiedi all'utente una stringa e produci la sua inversa
    """
    inversa = InvertiStringa()
    print(f'La stringa inversa è "{inversa}"')

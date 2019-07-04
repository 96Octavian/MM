import Compito1
import Compito2
import Compito3
import CompitoVacanze

if __name__ == '__main__':
    print("RACCOGLITORE DI COMPITI")

    choice = -1
    funz = [
        Compito1.chiedi_nome,
        Compito1.crea_csv_ma_migliore,
        Compito2.chiedi_nome,
        Compito3.chiedi_lista
    ]
    info = (
        '\n0 - crea_csv\n'
        '1 - crea_csv_ma_migliore\n'
        '2 - conta_parole\n'
        '3 - iniziali\n'
        '\n99 - Esci\n'
    )
    print(info)
    while choice != 99:
        tmp = input("Che funzione vuoi provare?\n")
        try:
            choice = int(tmp)
        except ValueError:
            print("Inserisci un numero")
            continue

        try:
            funz[choice]()
        except IndexError:
            print("Scelta non valida")

        print(info)
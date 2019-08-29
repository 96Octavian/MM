import scrivi_csv
import contatore
import iniziali

if __name__ == '__main__':
    print("RACCOGLITORE DI COMPITI")

    choice = -1
    funz = [
        scrivi_csv.chiedi_nome,
        scrivi_csv.crea_csv_ma_migliore,
        contatore.chiedi_nome,
        iniziali.chiedi_lista
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

    print("Addio!")
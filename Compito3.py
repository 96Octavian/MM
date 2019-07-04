#Scrivi una funzione iniziali(lista)che riceva una lista di stringhe.
#La funzione deve restituire solo le iniziali delle stringhe della lista di partenza che sono più lunghe di 8 caratteri.


def iniziali(lista):
    c=[]
    for i in lista:
        if len(i) > 8:
            c.append(i)
    for i in c:
        print (i[0])

def chiedi_lista():
    lista = []
    input_string = "s"
    while not lista or input_string:
        input_string = input("Inserisci una parola: ")
        if input_string: lista.append(str(input_string))
    iniziali(lista)

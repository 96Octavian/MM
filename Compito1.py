import csv


def crea_csv(filename):
	file_da_scrivere = open("output.csv", "w")
	file_da_leggere = open(filename, "r")
	scrittore = csv.writer(file_da_scrivere, delimiter=',')
	while True:
		scrivere = []
		for i in range(0,4):
			riga = file_da_leggere.readline().rstrip()
			if len(riga) > 0:
				scrivere.append(riga.split(":")[1])
			else:
				file_da_leggere.close()
				file_da_leggere.close()
				return None
		scrittore.writerow(scrivere)


def crea_csv_ma_migliore(filename):
	try:
		file_da_scrivere = open("output_ma_migliore.csv", "w", newline='')
		file_da_leggere = open(filename, "r")
	except FileNotFoundError:
		print("Nome file sbagliato")
		return 1
	colonne = ["nome", "cognome", "data di nascita", "luogo di nascita"]
	scrittore = csv.writer(file_da_scrivere, delimiter=',')
	scrittore.writerow(colonne)
	riga = []
	for line in file_da_leggere:
		if not line.rstrip():
			break
		riga.append(line.split(':')[1].rstrip())
		if len(riga) == 4:
			scrittore.writerow(riga)
			riga = []
	file_da_scrivere.close()
	file_da_leggere.close()


def chiedi_nome():
	filename = input("Che file devo aprire? ")
	crea_csv(filename)


def chiedi_nome_ma_migliore():
	filename = input("Che file devo aprire? ")
	crea_csv_ma_migliore(filename)


if __name__ == '__main__':
	crea_csv("Dati")
	crea_csv_ma_migliore("Dati")

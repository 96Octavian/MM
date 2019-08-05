import Compitone
Compitone.sommapercentuale()
f = open ("singolo", "r")
g = open ("duenomi", "r")
n=0
a=0
for i in f:
    n = int(float(i)) + n

for i in g:
    a = int(float(i)) + a
print(n)
print(a)
print(a+n)

nomefile = "valori1"
Compitone.creafile()
a = Compitone.contarighe(nomefile)
print(a)

import random
print('\nZAD1\n')
lista = []
a = 1
for a in range(50):
    a = random.randrange(100)
    if a % 4 == 0:
        lista.append(a)
print(lista)
plik = open("pd4.txt", "w+")
plik.writelines(str(lista))
plik.close()
print('\n\n')


print('\nZAD2\n')
plik = open("pd4.txt", "r")
x = plik.readlines()
plik.close()
print(x)
print('\n\n')

print('\nZAD3\n')

with open('plik.txt', 'a') as a:
    for elem in 'REALMADRYT':
        a.write(elem + '\n')

with open('plik.txt', 'r') as b:
    for elem in b:
        print(elem[:-1])

print('------zadanie 4------')
class NaZakupy:

    def __init__(self, nazwa, ilosc,cena,jednostka ):
        self.nazwa = nazwa
        self.ilosc = ilosc
        self.jednostka = jednostka
        self.cena = cena

    def wyswietl_produkt(self):
        return self.nazwa

    def ile_produktu(self):
         return f'{self.ilosc}  {self.jednostka}'

    def ile_kosztuje(self):
        return self.ilosc * self.cena

x = NaZakupy("jajka", 20,0.6, "szt")
y = NaZakupy("mango", 3,2.90, "szt")

print(x.wyswietl_produkt())
print(y.ile_kosztuje())
print(y.ile_produktu())
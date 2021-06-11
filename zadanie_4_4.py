"""### Zadanie 4.4 | Zbiornik

Stwórz klasę `Zbiornik`. Niech ta klasa ma tylko jeden atrybut: `ilosc_wody` (z początkową wartością 0).
Niech ta klasa ma metody `dolej` i `odlej`. Obie metody niech przyjmują argument `ile` i niech odpowiednio dodają
lub odejmują tę liczbę do atrybutu `ilosc_wody`. Niech nie da się odlać więcej wody, niż jest w zbiorniku.
Niech obiekt klasy `Zbiornik` po skonwertowaniu na napis dawał napis `zbiornik z (ileś tam) litrami wody`.
Przerób klasę `Zbiornik` tak, żeby miała też drugi atrybut - `temperatura`.
Metoda dolej oprócz argumentu `ile` powinna też przyjmować argument `temperatura` oznaczający temperaturę dolewanej wody.
Dolanie wody do zbiornika powinno powodować zmianę temperatury wody w zbiorniku (zgodnie ze zwykłymi prawami fizyki)."""

class Zbiornik:
    ILOSC_WODY = 0
    TEMPERATURA = 0

    def dolej(self, ile, temp):
        if self.TEMPERATURA == 0:
            self.TEMPERATURA = temp
        else:
            self.TEMPERATURA = (ile * temp + self.ILOSC_WODY * self.TEMPERATURA) / (ile + self.ILOSC_WODY)
        self.ILOSC_WODY += ile

    def odlej(self, ile):
        if ile > self.ILOSC_WODY:
            print("Nie można odlać wskazanej ilości wody!")
        else:
            self.ILOSC_WODY -= ile

    def __str__(self):
        return f'Zbiornik z {self.ILOSC_WODY} ilością wody. Temperatura wody wynosi: {self.TEMPERATURA:.2f} stopni.'

z = Zbiornik()
z.dolej(40, 40)
print(z)
z.dolej(130, 10)
print(z)
z.odlej(50)
print(z)
z.dolej(100, 100)
print(z)
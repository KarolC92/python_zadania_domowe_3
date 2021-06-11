"""### Zadanie 4.5 | Żółw

Napisz klasę `Zolw` z metodami `idz` i `obroc_sie`. Żółw ma jakieś położenie (wyrażone dwiema współrzędnymi)
i jakieś ustawienie, czyli kurs (wyznaczony pojedyncza liczba).
Początkowe położenie podajemy konstruktorowi klasy, początkowy kurs to zawsze 0.
Metoda `obroc_sie ` powoduje obrót żółwia, czyli zmianę jego kursu.
Metoda `idz` powoduje przejście żółwia o określoną odległość.
Z klasy będzie się korzystać tak:

```python
z = Zolw(100, 100)
z.idz(50)
print(z) # ma sie wypisac: x=100, y=50
z.obroc_sie(90)
z.idz(50)
print(z) # ma sie wypisac: x=150, y=50"""
import math

class Zolw:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.kierunek = 0

    def idz(self, ile):
        self.x += math.sin(math.radians(self.kierunek)) * ile
        self.y -= math.cos(math.radians(self.kierunek)) * ile

    def obroc_sie(self, ile):
        self.kierunek += ile

    def __str__(self):
        return f'x = {self.x:.2f}, y = {self.y:.2f}'

z = Zolw(100, 100)
print(z)
z.idz(50)
print(z)
z.obroc_sie(90)
z.idz(50)
print(z)
z.obroc_sie(20)
z.idz(30)
print(z)
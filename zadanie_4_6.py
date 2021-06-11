"""### Zadanie 4.6 | Kółko i krzyżyk

Stwórz klasę `PlanszaXO` - jej obiekty mają reprezentować stan planszy do gry w kółko i krzyżyk.
Ma ona mieć metody:
`dodaj_element(x: int, y: int, rodzaj_elementu)`
W argumencie `rodzaj_elementu` będzie napis `"x"` lub `"o"`. Jeśli ruch jest nieprawidłowy, metoda powinna zwracać fałsz.
`stan_gry()`
Ta metoda ma zwracać liczbę oznaczającą stan gry (gra trwa, gra zakończona sukcesem krzyżyków, gra zakończona sukcesem kółek).
`czyj_ruch()`
Ta metoda ma powiedzieć, czyj ruch ma być teraz (kółek czy krzyżyków).
Wyświetlenie obiektu tej klasy ma wypisać planszę.
Użyj tej klasy do zrobienia gry w kółko i krzyżyk."""
import random


class PlanszaXO:
    def __init__(self):
        self.plansza = [['', '', ''], ['', '', ''], ['', '', '']]
        self.ostatni_ruch = ''
        self.kto_zaczyna = ''

    def dodaj_element(self, x: int, y: int, rodzaj_elementu: str):
        if isinstance(x, int) and isinstance(y, int):
            if x < 0 or x > 2 or y < 0 or y > 2:
                return False
            if rodzaj_elementu not in ['X', 'O']:
                return False
            if self.ostatni_ruch == '':
                if self.kto_zaczyna != rodzaj_elementu:
                    return False
            if self.ostatni_ruch == 'X' and rodzaj_elementu == 'X':
                return False
            if self.plansza[x][y] != '':
                print('Obszar zajęty')
                return False
            else:
                self.plansza[x][y] = rodzaj_elementu
                self.ostatni_ruch = rodzaj_elementu
        else:
            raise ValueError(f'ValueError')

    def sprawdz_rzedy(self, p, z):
        return any([{z} == set(p[i]) for i in range(3)])

    def sprawdz_skosy(self, z):
        return {z} == set(self.plansza[i][i] for i in range(3)) or {z} == set(self.plansza[i][2-i] for i in range(3))

    def obroc_plansze(self):
        return [[self.plansza[i][j] for i in range(3)] for j in range(3)]

    def stan_gry(self):
        if self.sprawdz_rzedy(self.plansza, 'X') or self.sprawdz_rzedy(self.obroc_plansze(), 'X') or self.sprawdz_skosy('X'):
            return 'krzyżyki wygrywają'
        if self.sprawdz_rzedy(self.plansza, 'O') or self.sprawdz_rzedy(self.obroc_plansze(), 'O') or self.sprawdz_skosy('O'):
            return 'kółka wygrywają'
        if any('' in self.plansza[i] for i in range(3)):
            return 'Gra trwa'
        else:
            return 'Remis'


    def czyj_ruch(self):
        ruch = ['X', 'O']
        if self.ostatni_ruch == 'X':
            return f'Ruch {"O"}'
        elif self.ostatni_ruch == 'O':
            return f'Ruch {"X"}'
        else:
            self.kto_zaczyna = random.choice(ruch)
            return f'Ruch {self.kto_zaczyna}'

    def __str__(self):
        return f'{" "* 60}\n' \
               f'     |       |     \n'\
               f'  {self.plansza[0][0].center(2)} | {self.plansza[0][1].center(5)} | {self.plansza[0][2].center(4)}\n' \
               f'-----|-------|-----\n' \
               f'  {self.plansza[1][0].center(2)} | {self.plansza[1][1].center(5)} | {self.plansza[1][2].center(4)}\n' \
               f'-----|-------|-----\n' \
               f'  {self.plansza[2][0].center(2)} | {self.plansza[2][1].center(5)} | {self.plansza[2][2].center(4)}\n' \
               f'     |       |     \n' \
               f'{" "* 60}\n' \
               f'{self.czyj_ruch()}\n' \
               f'{self.stan_gry()}\n'


p = PlanszaXO()
while True:
    if p.stan_gry() == 'Gra trwa':
        print(p)
        x = -1
        y = -1
        while x == -1 and y == -1:
            try:
                x = int(input('Podaj x: '))
            except ValueError:
                print('Złe dane')

            try:
                y = int(input('Podaj y: '))
            except ValueError:
                print('Złe dane')
        element = input('Podaj element: ').upper()
        p.dodaj_element(x, y, element)
    else:
        print(p)
        break


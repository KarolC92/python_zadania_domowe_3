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

    def stan_gry(self):

        stan_1 = f'krzyżyki wygrywają'
        stan_2 = f'kółka wygrywają'
        stan_3 = f'Gra trwa'
        licz_skos_x = 0
        licz_skos_o = 0
        licz_poziom_x = 0
        licz_poziom_o = 0
        licz_pion_x = 0
        licz_pion_o = 0

        for i in range(3):
            for j in range(3):
                if i == j:
                    if self.plansza[i][j] == 'X':
                        licz_skos_x += 1
                        if licz_skos_x == 3:
                            return stan_1
                    elif self.plansza[i][j] == 'O':
                        licz_skos_o += 1
                        if licz_skos_o == 3:
                            return stan_2
                if self.plansza[i][j] == 'X':
                    licz_poziom_x += 1
                    if licz_poziom_x == 3:
                        return stan_1
                if self.plansza[i][j] == 'O':
                    licz_poziom_o += 0
                    if licz_poziom_o == 3:
                        return stan_2
                if self.plansza[j][i] == 'X':
                    licz_pion_x += 1
                    if licz_pion_x == 3:
                        return stan_1
                if self.plansza[j][i] == 'O':
                    licz_pion_o += 1
                    if licz_pion_o == 3:
                        return stan_2

            licz_poziom_x = 0
            licz_poziom_o = 0
            licz_pion_x = 0
            licz_pion_o = 0

        return stan_3

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


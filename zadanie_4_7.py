"""### Zadanie 4.7 | Ogłoszenia / dziedziczenie

Do zadania z klasą `Ogloszenie` dodaj kolejne klasy, które po niej dziedziczą.
`OgloszenieSamochodowe` – dziedziczy z `Ogloszenie` i dodatkowo określa cechy sprzedawanego samochodu jak model, markę,
rok produkcji, przebieg, pojemność, moc i rodzaj paliwa.
`OgloszenieMieszkaniowe` – też dziedziczy z `Ogloszenie`, a dodatkowo cechy sprzedawanego mieszkania / domu: miejscowość,
metraż, liczba pokoi."""


class ContactDetails:
    def __init__(self, name: str, tel: str, mail: str):
        self.name = name
        self.tel = tel
        self.mail = mail

    def __str__(self):
        return f'name: {self.name}, tel: {self.tel[0:3]}-{self.tel[3:6]}-{self.tel[6:]}, mail: {self.mail}'


class Advertisement:
    def __init__(self, title, description, price, seller: ContactDetails) -> object:
        self.title = title
        self.description = description
        self.price = price
        self.seller = seller

    def __str__(self):
        return f'Title: {self.title}\n' \
               f'Description: {self.description}\n' \
               f'Price: {self.price}\n' \
               f'Seller: {self.seller}'

class OgloszenieSamochodowe(Advertisement):
    def __init__(self, title, description, price, seller: ContactDetails, model, marka, rok_produkcji, przebieg, pojemnosc, moc, rodzaj_paliwa):
        super().__init__(title, description, price, seller)
        self.model = model
        self.marka = marka
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg
        self.pojemnosc = pojemnosc
        self.moc = moc
        self.rodzaj_paliwa = rodzaj_paliwa

    def __str__(self):
        return f'{self.title}, {self.description}, {self.price}, {self.seller}\n' \
               f'model: {self.model}, marka: {self.marka}, rok produkcji: {self.rok_produkcji} rok,\n' \
               f'przebieg: {self.przebieg} km., pojemność: {self.pojemnosc} l., moc: {self.moc} KM., paliwo: {self.rodzaj_paliwa}'

c = ContactDetails('Karol', '111222333', 'k@gmail.com')
a = Advertisement('Ogloszenie', 'aaaaa bbbbbb ccccc bdddddd', 4500, c)
o = OgloszenieSamochodowe('Ogloszenie', 'aaaaaa bbbbbb ccc ddddddddd,', 4500, c, 'Focus', 'Ford', 2005, 199000, 1.8, 115, 'Diesel')
print(o)
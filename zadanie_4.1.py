"""### Zadanie 4.1 | Ogłoszenia

Zaproponuj klasę, w której obiektach będzie się zapisywać ogłoszenia (takie jak w serwisie internetowym z ogłoszeniami).
Najlepiej, aby klasa `Ogloszenie` opisywała rzeczy, które posiada każde ogłoszenie, m.in.
tytuł, opis, cenę, dane kontaktowe sprzedawcy."""


class ContactDetails:
    def __init__(self, name, tel, mail):
        self.name = name
        self.tel = tel
        self.mail = mail

    def __str__(self):
        return f'name: {self.name}, tel: {self.tel}, mail: {self.mail}'


class Advertisement:
    def __init__(self, title, description, price, seller: ContactDetails):
        self.title = title
        self.description = description
        self.price = price
        self.seller = seller

    def __str__(self):
        return f'Title: {self.title}\n' \
               f'Description: {self.description}\n' \
               f'Price: {self.price}\n' \
               f'Seller: {self.seller}'

s_1 = ContactDetails('Karol', '881495856', 'k_c@gmail.com')
a_1 = Advertisement('Sprzedaż auta', 'Sprzedaż samochodu marki Ford', 1999, s_1)
print(a_1)
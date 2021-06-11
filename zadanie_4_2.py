"""### Zadanie 4.2 | Lista ogłoszeń

Napisz programy, w których tworzysz listę ogłoszeń samochodowych,
a następnie wyszukujesz ogłoszenia na podstawie ich parametrów.
Na przykład ogłoszenia o cenach z określonego przedziału.
Użyj funkcji `lambda`, określających, które ogłoszenia powinny zostać wyszukane.
Użyj poznanych kolekcji do trzymania ogłoszeń. Możesz zastosować metodę `filter` do wyszukiwania odpowiednich ogłoszeń."""

import random

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
               f'Description: {self.description[:10]}\n' \
               f'Price: {self.price}\n' \
               f'Seller: {self.seller}'


def price_filter(min_price, max_price, list_advert):
    return list(filter(lambda x: min_price <= x.price <= max_price, list_advert))

def phone_filter(phone_numbers: str, list_advert):
    return list(filter(lambda x: x.seller.tel == phone_numbers, list_advert))



names = ['Karol', 'Konrad', 'Janusz', 'Mariusz', 'Jakub']
phone_numbers = ['111222333', '222333444', '333444555', '444555666', '555666777']
mails = ['ka@gmail.com', 'ko@gmail.com', 'ja@gmail.com', 'ma@gmail.com', 'jak@gmail.com']

descriptions = ['aaaaaaaa aaaaaaaa aaaaaaaa aaaaaaaaa',
                'bbbbbbbb bbbbbbbb bbbbbbbb bbbbbbbbb',
                'cccccccc cccccccc cccccccc ccccccccc',
                'dddddddd dddddddd dddddddd ddddddddd',
                'eeeeeeee eeeeeeee eeeeeeee eeeeeeeee']

titles = ['Sprzedam Opla',
          'Sprzedam Forda',
          'Sprzedam Skode',
          'Sprzedam Fiata',
          'Sprzedam Tico']

advert_list = []
for i in range(10):
    s = ContactDetails(random.choice(names), random.choice(phone_numbers), random.choice(mails))
    a = Advertisement(random.choice(titles), random.choice(descriptions), random.randint(5000, 80000), s)
    advert_list.append(a)

result_p = phone_filter('222333444', advert_list)
for i in result_p:
    print(i)
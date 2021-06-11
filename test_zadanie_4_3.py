from unittest import TestCase
from zadanie_4_3 import Pociag


class TestPociag(TestCase):
    def test_init(self):
        t1 = Pociag()
        self.assertEqual(t1.predkosc, 10)
        self.assertEqual(t1.ilosc_paliwa, 1000)
        t2 = Pociag(predkosc=20, ilosc_paliwa=30)
        self.assertEqual(t2.predkosc, 20)
        self.assertEqual(t2.ilosc_paliwa, 30)

    def test_przyspiesz(self):
        t = Pociag(predkosc=20)
        t.przyspiesz(5)

    def test_opis(self):
        pass

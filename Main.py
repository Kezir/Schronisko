from Pracownik import *
from Klatka import *
from Pracownicy_db import *

def main():
    #pracownik1 = Pracownik("Dariusz","Gąbrowski","kierowca","dariuszgabrowski@gmail.com","790039234")
    #pracownik2 = Pracownik("Michał","Nisko","pracownik biurowy","michalnisko@gmail.com","780234222")
    #for i in range(20):
    #    Klatka()
    Czytaj_dane()
    print(Wyszukaj_pracownika("780234222"))
    print(Wyszukaj_klatke(20))
    Dodaj_zwierzaka("20","1")
    Dodaj_zwierzaka("20","2")
    print(Wyszukaj_klatke(20))

main()
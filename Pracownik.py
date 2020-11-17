from Pracownicy_db import *

class Pracownik:
    def __init__(self, imie, nazwisko, stanowisko, email, telefon):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stanowisko = stanowisko
        self.email = email
        self.telefon = telefon
        self.zarejestruj()

    def zarejestruj(self):
        cur.execute('INSERT INTO pracownicy (imie,nazwisko,stanowisko,email,telefon) VALUES(?,?,?,?,?)', (self.imie,self.nazwisko,self.stanowisko,self.email,self.telefon))
        con.commit()
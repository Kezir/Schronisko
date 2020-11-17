import sqlite3

con = sqlite3.connect('sample.db')

cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS pracownicy (
        id INTEGER PRIMARY KEY,
        imie varchar(250) NOT NULL,
        nazwisko varchar(250) NOT NULL,
        stanowisko varchar(250) NOT NULL,
        email varchar(250) NOT NULL,
        telefon varchar(250) NOT NULL
)""")

def Czytaj_dane():
    cur.execute("""
        SELECT * FROM pracownicy
    """)
    pracownicy = cur.fetchall()
    for dane in pracownicy:
        print(dane)

def Wyszukaj_pracownika(wartosc):
    cur.execute("""
            SELECT * FROM pracownicy
        """)
    pracownicy = cur.fetchall()
    for dane in pracownicy:
        for i in dane:
            if(i == wartosc):
                return dane

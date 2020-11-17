import sqlite3

con = sqlite3.connect('sample2.db')

cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS schronisko (
        id INTEGER PRIMARY KEY,
        stan varchar(250) NOT NULL,
        karma varchar(250) NOT NULL,
        zwierzaki varchar(250)
)""")

def Czytaj_dane():
    cur.execute("""
        SELECT * FROM schronisko
    """)
    schronisko = cur.fetchall()
    for dane in schronisko:
        print(dane)

def Wyszukaj_klatke(nr_klatki):
    cur.execute("""
            SELECT * FROM schronisko
        """)
    pracownicy = cur.fetchall()
    for dane in pracownicy:
        if dane[0] == nr_klatki:
            return dane

def Dodaj_zwierzaka(id_klatki,id_zwierzaka):
    cur.execute("UPDATE schronisko SET zwierzaki = zwierzaki || ? || ? WHERE id = ?", (id_zwierzaka," ",id_klatki))

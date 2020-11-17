from Schronisko_db import *

class Klatka:
    def __init__(self):
        self.stan = "dobry"
        self.karma = "0"
        self.stworz_klatke()

    def stworz_klatke(self):
        cur.execute('INSERT INTO schronisko (stan,karma,zwierzaki) VALUES(?,?,?)', (self.stan,self.karma,""))
        con.commit()
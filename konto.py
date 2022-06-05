
import datetime
from datetime import date
#from datetime import datetime


###konto
class Konto:
    def __init__(self, nr, klient, stan=0, historia=([])):
        self._nr = nr
        self._klient = klient
        self._stan = stan
        self._historia = historia

    def wpłata(self, wartosc):
        self._stan += wartosc
        self._historia.append(["wplata", wartosc, date.today(), self._stan])

    def wypłata(self, wartosc):
        self._stan -= wartosc
        self._historia.append(["wyplata", -wartosc, date.today(), self._stan])
      
    def drukHistorii(self, data):
        print('Konto:', self._nr, 'Stan: 0.00')
        for i in range(len(self._historia)):
            if data < self._historia[i][2]:
                print("{:.2f}".format(self._historia[i][1]), self._historia[i][2].strftime('%d-%m-%Y'), "{:.2f}".format(self._historia[i][3]))
            else: 
                continue
    


###konto limitowane
class KontoLimitowane(Konto):
    def __init__(self, nr, klient, stan=0, historia=([]), limit=0):
        self._nr = nr
        self._klient = klient
        self._stan = stan
        self._historia = historia
        self._limit = limit

    def wpłata(self, wartosc):
        self._stan += wartosc
        self._limit += wartosc
        self._historia.append(["wplata", wartosc, date.today(), self._stan])

    def wypłata(self, wartosc):
        self._stan -= wartosc
        self._limit -= wartosc
        if self._limit >= 0:
            self._historia.append(["wyplata", -wartosc, date.today(), self._stan])
        else: 
            print('Brak srodkow na koncie: ', self._nr, 'na wyplate', "{:.2f}".format(wartosc))
             
    def drukHistorii(self, data):
        print('Konto:', self._nr, 'Stan: 0.00')
        for i in range(len(self._historia)):
            if data < self._historia[i][2]:
                print("{:.2f}".format(self._historia[i][1]), self._historia[i][2].strftime('%d-%m-%Y'), "{:.2f}".format(self._historia[i][3]))
            else: 
                continue

##wywolanie
if __name__ == '__main__':
    import konto as k
    k1 = k.Konto('11001100', 'Jan')
    k1.wpłata(1_200)
    k1.wpłata(2_300)
    k1.wypłata(4_000)
    k1.drukHistorii(datetime.date(2021,10,4))
    k2 = k.KontoLimitowane('11002273','Anna')
    k2.wpłata(1_200)
    k2.wpłata(2_300)
    k2.wypłata(4_000)
    k2.drukHistorii(datetime.date(2021,10,4))


        


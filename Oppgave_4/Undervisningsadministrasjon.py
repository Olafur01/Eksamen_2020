from Dato import Dato
from Student import Student
from Aktivitet import Aktivitet
from Emne import Emne


class Undervisningsadministrasjon:
    def __init__(self):
        self._emner = {}
        self._datoer = {}
        self._studenter = {}

    def lesFilF(self, filnavn):
        filen = open(filnavn, 'r')
        for linje in filen:
            linje = linje.split()
            if linje[0] not in self._emner:
                self._emner[linje[0]] = Emne(linje[0])
                Emne(linje[0]).leggTilAktivitet(linje[1])
            else:
                Emne(linje[0]).leggTilAktivitet(linje[1])
            dato = Dato(linje[2], linje[3], linje[4])
            if dato not in self._datoer:
                self._datoer[dato.absoluttDato()] = [dato]
            else:
                self._datoer[dato.absoluttDato()].append(dato)
            linje[1] = Aktivitet(linje[0], dato, linje[1])

        filen.close()

    def lesFilG(self, filnavn):
        filen = open(filnavn, 'r')
        for linje in filen:
            linje = linje.split()
            if linje[0] not in self._studenter:
                self._studenter[linje[0]] = Student(linje[0])
            else:
                pass
            if linje[1] in self._emner.keys():
                linje[2].leggTilRegistertStudent()
            else:
                pass
        filen.close()

    # Mulig resten av koden ikke fungere slik den skal, men hvis den gjoer det
    # saa skal alle verdiene i self._emne peker aktivitet hvor man kan da kalle
    # paa mottopp funksjonen for aa se hvor mange som har blitt med.
    def skrivGrupperMedHoytOppmoete(self, antall):
        for values in self._emner.values():
            if values._mottopp > antall:
                print(f' I {values} har det mott opp {values._mottopp}')
            else:
                continue


txt = 'text.csv'
undervisning = Undervisningsadministrasjon()
undervisning.lesFilF(txt)

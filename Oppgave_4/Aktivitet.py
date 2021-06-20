from Dato import Dato
from Student import Student


class Aktivitet:
    def __init__(self, emne, dato, aktivitetsnummer):
        self._emne = emne
        self._dato = dato
        self._aktivitetsnummer = aktivitetsnummer
        self._registert = []
        self._mottopp = []

    def leggTilRegistertStudent(self, student):
        self._registert.append(student)

    def registrerOppmote(self, student):
        self._mottopp.append(student)

    def skrivUtOppmotteStudenter(self):
        for student in self._mottopp:
            print(student)

    def absoluttDato(self):
        return self._dato.absoluttDato()

    def oppmott(self):
        return f"{len(self._mottopp)} student(er) har mott opp til dette emne"

    def __str__(self):
        return f"{self._emne} har aktivitetsnummer {self._aktivitetsnummer} og {self.oppmott()} student(er) har mott opp"


dato = Dato(30, 12, 20)
emne = "IN1000"
aktivitetsnummer = 1
olav = Student('ogbrokke')
luca = Student('luca')
sondre = Student('sondre')
in1000 = Aktivitet(emne, dato, aktivitetsnummer)
in1000.registrerOppmote(olav.hentBrukernavn())
in1000.registrerOppmote(luca.hentBrukernavn())
in1000.registrerOppmote(sondre.hentBrukernavn())
in1000.skrivUtOppmotteStudenter()
print(in1000.absoluttDato())
print(in1000.oppmott())
print(in1000)

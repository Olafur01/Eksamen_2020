class Emne:
    def __init__(self, kode):
        self._kode = kode
        self._aktiviter = []

    def leggTilAktivitet(self, aktivitet):
        self._aktiviter.append(aktivitet)

    def returkode(self):
        return self._kode


in1000 = Emne('In1000')
in1000.leggTilAktivitet("Oblig1")
in1000.leggTilAktivitet("Oblig2")
in1000.leggTilAktivitet("Oblig3")
print(in1000)

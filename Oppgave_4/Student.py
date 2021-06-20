class Student:
    def __init__(self, brukernavn):
        self._brukernavn = brukernavn

    def hentBrukernavn(self):
        return self._brukernavn


# olav = Student('ogbrokke')

# print(olav.hentBrukernavn())

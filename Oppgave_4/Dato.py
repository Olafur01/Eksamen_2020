class Dato:
    def __init__(self, dag, maaned, aar):
        self._dag = dag
        self._maaned = maaned
        self._aar = aar

    def absoluttDato(self):
        maaned = self._maaned
        dag = self._dag
        if len(str(maaned)) < 2:
            maaned = '0' + str(self._maaned)
        if len(str(dag)) < 2:
            dag = '0' + str(self._dag)
        return f"{maaned}{dag}{self._aar}"

    def __str__(self):
        maaned = ''
        if self._maaned == 8:
            maaned = 'august'
        elif self._maaned == 9:
            maaned = 'september'
        elif self._maaned == 10:
            maaned = 'oktober'
        elif self._maaned == 11:
            maaned = 'november'
        elif self._maaned == 12:
            maaned = 'desember'
        else:
            return "Denne maaneden er ikke paa hostsemesteret"
        return f"{self._dag}. {maaned} 20{self._aar}"


variable = Dato(30, 12, 20)
print(variable.absoluttDato())
print(variable)

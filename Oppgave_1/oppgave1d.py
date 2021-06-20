class Info:

    def __init__(self, x):

        self._alder = 2021 - x

    def __str__(self):
        return str(self._alder)


petter = Info(2000)
print(petter)

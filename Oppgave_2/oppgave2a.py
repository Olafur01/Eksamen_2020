class Ukedag:
    def __init__(self, dag):
        self.dag = dag


torsdag = Ukedag(4)
imorgen = Ukedag(4 + 1)
fredag = imorgen
helg = Ukedag(6)
fredag = None
helg = None
lordag = helg

print(lordag)
print(fredag)
print(torsdag)
print(imorgen)
print(helg)

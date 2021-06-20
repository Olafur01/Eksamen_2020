'''Skriv en funksjon fridager(julaften) som returnerer antall fridager fra og med 25. desember, til og med 31. desember.
Det er alltid fri lørdag og søndag, dessuten 25. og 26. desember. Om noen av disse faller på samme dag blir det færre enn 4 dager fri. Julaften er 24. desember.

Parameteren julaften skal inneholde en streng som angir hvilken ukedag julaften faller på. Det vil si at kallet fridager("sondag") skal evaluere til 4, mens fridager("fredag") skal evaluere til 2.'''


def fridager(julaften):
    julaften = julaften.lower()
    if julaften == 'sondag':
        return 4
    elif julaften == 'mandag':
        return 4
    elif julaften == 'tirsdag':
        return 4
    elif julaften == 'onsdag':
        return 4
    elif julaften == 'torsdag':
        return 3
    elif julaften == 'fredag':
        return 2
    elif julaften == 'lordag':
        return 3


print(fridager("sondag"))
fridager("fredag")

def beOmNavn(navneliste):
    navn = ''
    while navn not in navneliste:
        navn = input('Skriv inn et navn: ')
        if navn in navneliste:
            return navn
        else:
            continue


navneliste = ['olav', 'luca', 'sondre']

print(beOmNavn(navneliste))

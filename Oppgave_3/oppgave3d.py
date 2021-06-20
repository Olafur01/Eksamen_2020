def stringFraInt(tall):
    tall = str(tall)
    returtall = tall
    if len(tall) == 1:
        returtall = '00000' + tall


def intTilString(tall, antallSiffer):
    tall = str(tall)
    returtall = tall
    if len(tall) == antallSiffer:
        return returtall
    elif len(tall) < antallSiffer:
        returtall = "0" * (antallSiffer - len(tall)) + tall
        return returtall
    else:
        return returtall


print(intTilString(87, 4))
assert intTilString(87, 4) == '0087'
assert intTilString(87, 2) == '87'
assert intTilString(87, 1) == '87'
assert intTilString(1, 11) == '00000000001'
assert intTilString(0, 2) == '00'
assert intTilString(0, 0) == '0'

print(intTilString(87, 2))
print(intTilString(87, 1))
print(intTilString(1, 11))
print(intTilString(0, 2))
print(intTilString(0, 0))

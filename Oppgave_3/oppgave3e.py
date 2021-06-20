def dempDeg(tekst):
    tekst = tekst.strip('!')
    if tekst[-1] == '.':
        return tekst
    else:
        tekst = tekst + '.'
        return tekst

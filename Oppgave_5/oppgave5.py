def lagSynonymordbok(listeAvListe):
    ordbok = {}
    for i in listeAvListe:
        for l in i:
            if l not in ordbok:
                liste1 = []
                for r in i:
                    if r != l:
                        liste1.append(r)
                    else:
                        pass
                ordbok[l] = [liste1]
            else:
                liste2 = []
                for r in i:
                    if r != l:
                        liste2.append(r)
                    else:
                        pass
                ordbok[l].append(liste2)
    return ordbok


synonymer = [['a', 'e', 'i', 'o', 'u'], ['HOM', 'c', 'd'],
             ['y', 'HOM'], ['k', 'l', 'm', 'n', 'p', 'q'], ['x']]

ordbok = lagSynonymordbok(synonymer)
print(ordbok['e'])

print(ordbok['HOM'])

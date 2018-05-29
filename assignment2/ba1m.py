#Zuordnen von Nucleotide zu Zahlen
def NumToSym(num):
    NTS = {0:'A', 1:'C', 2:'G', 3:'T'}
    return NTS[num]
#Umwandeln von Zahl in Nucleotidreihe
def NumToPat(index,k):
    if k == 1:
        return NumToSym(index)
    prefIndex = int(index/4)
    r = index%4
    sym = NumToSym(r)
    prefPat = NumToPat(prefIndex,k-1)
    return prefPat + sym
#Ausgabe
print(NumToPat(45,4))

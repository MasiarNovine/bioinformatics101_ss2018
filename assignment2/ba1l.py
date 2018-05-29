#Zuordnen von Zahlen zu Nucleotiden
def SymToNum(sym):
    STN = {'A':0,'C':1,'G':2,'T':3}
    return STN[sym]
#Umwandeln von Nucleotidreihenfolge in Zahl
def PatToNum(Pat):
    if not Pat:
        return 0
    sym = Pat[-1]
    pref = Pat[0:-1]
    return ((4*PatToNum(pref))+SymToNum(sym))
#Ausgabe
print(PatToNum('AGT'))

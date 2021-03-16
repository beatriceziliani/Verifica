
def firma():
    Verifica.firma("Beatrice Ziliani")

def svolgiEs(n_esercizio):
    es=Verifica.inizia_esercizio(n_esercizio)
    dati = es.dati
    soluzione = es1(dati)
    es.consegna(soluzione)


def es1(dati):
    ...#esercizio da svolgere
    return dati
    


#firma()
#svolgiEs(1)

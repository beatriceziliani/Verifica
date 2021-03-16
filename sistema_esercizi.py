# Se la libreria spalla non e' installata eseguire sul terminale il comando `pip install spalla --user`

from spalla import Verifica # importi la libreria

Verifica.firma("Nome Cognome") # firmi la verifica, questa operazione è obbligatoria almeno una volta

Verifica.stampa_esercizi() # stampa sul terminale l'elenco degli esercizi disponibili in questa verifica

Verifica.stampa_voto() # stampa il vostro voto attuale

es = Verifica.inizia_esercizio(1) # restituisce l'esercizio numero 1

print(es) # mostra la consegna dell'esercizio e i dati sui quali lavorare, è una raccolta dati complessa, quindi inutilizzabile

print(es.dati) # restituisce i dati dell'eserizio in una forma primitiva (stringa, lista, intero, float, dizionario, etc..)

x=es.dati*2  #si svolge la richiesta dell'esercizio, in questo caso di moltiplicare il dato per 2

es.consegna(x) # viene consegnato il risultato (in questo caso la variabile x)
               #La consegna può restituire esercizio corretto (+ un punto)
               #Oppure crasha il programma (non c'è da preoccuparsi) e viene restituito risposta sbagliata


#Esempio di come svolgere un esercizio

from spalla import Verifica

def firma():
    Verifica.firma("nome cognome")

def es2():
    es=Verifica.inizia_esercizio(2)
    dato=es.dati
    soluzione=dato**2  #si prende che la consegna fosse di elevare alla seconda il numero
    es.consegna(soluzione)

es2()   #viene richiamata la funzione dell'esercizio

from database.DAO import DAO #lo importi tu


class Model:
    def __init__(self):
        pass

    def getCodins(self):
        return DAO.getCodins()

    def getAllCorsi(self):
        return DAO.getAllCorsi()

    def getCorsiPD(self, pd):
        return DAO.getCorsiPD(pd)

    def getCorsiPDwithIscritti(self, pd):
        return DAO.getCorsiPDwithIscritti(pd)

    def getStudentiPerCorso(self, codins):
        #esempio --> stampa in ordine di cognome
        studenti = DAO.getStudentiPerCorso(codins)
        studenti.sort( key=lambda s: s.cognome)
        return studenti
        #lambda è un costrutto per definire una funzione senza nome
        #prende come argomento s e restituisce s.cognome
        #la sort farà l'ordinamento secondo la key quindi cognome

    def getCDSperCorso(self, codins):
        #ordina per numuero di iscritti (dal più grande al più piccolo)
        cds= DAO.getCDSperCorso(codins)
        cds.sort( key=lambda c: c[1], reverse=True )
        return cds
from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente


class DAO(): #def init non serve nel DAO

   #----------------------------------------------------------------------------------------------------------------------------
   @staticmethod
   def getCodins():
       cnx= DBConnect.get_connection()
       ris = []
       if cnx is None:
           print("No database connected")
           return ris
       else:
           cursor = cnx.cursor(dictionary=True)
           query= """SELECT c.codins
                      FROM corso c """
           cursor.execute(query)

           for row in cursor:
               ris.append(row["codins"]) #altirmenti senza dict=True sarebbe una tupla
                                         # e quindi devo prendere il primo elemento devi fare row[0]

           cursor.close()
           cnx.close()
           return ris

   # ----------------------------------------------------------------------------------------------------------------------------
   @staticmethod
   def getAllCorsi():
       cnx = DBConnect.get_connection()
       ris = []
       if cnx is None:
           print("Connessione fallita")
           return ris
       else:
           cursor = cnx.cursor(dictionary=True)
           query = """SELECT *
                      FROM corso c """
           cursor.execute(query)

           for row in cursor:
               #ris.append( Corso( codins=row["codins"], crediti=row["crediti"], nome=row["nome"], pd=row["pd"] ))
               #voglio l'oggetto Corso --> importo, e poi codins è uguale all'oggetto del ciclo da cui prendo uno specifico campo dato che row è un dizionario
               ris.append( Corso(**row))
           cursor.close()
           cnx.close()
           return ris

    #----------------------------------------------------------------------------------------------------------------------------
   @staticmethod
   def getCorsiPD(pd):
       cnx= DBConnect.get_connection()
       ris = []
       if cnx is None:
           print("Connessione fallita")
           return ris
       else:
           cursor = cnx.cursor(dictionary=True)
           query= """SELECT *
                    FROM corso c 
                    WHERE c.pd=%s"""   #%s è un parametro della stringa --> senza virgolette
           cursor.execute(query, (pd,) )

           for row in cursor:
               ris.append( Corso(**row))
           cursor.close()
           cnx.close()
           return ris

   # ----------------------------------------------------------------------------------------------------------------------------
   @staticmethod
   def getCorsiPDwithIscritti(pd):

       cnx= DBConnect.get_connection()
       ris = []
       if cnx is None:
           print("Connessione fallita")
           return ris
       else:
           cursor = cnx.cursor(dictionary=True)
           query= """SELECT c.codins, c.crediti, c.nome, c.pd, count(*) as n
                     FROM corso c, iscrizione i
                     WHERE c.codins = i.codins 
                     and c.pd=%s
                     group by c.codins, c.crediti, c.nome , c.pd"""
           cursor.execute(query, (pd, ))

           for row in cursor:
               #non possiamo prendere l'oggetto corso, ma dobbiamo prendere ogni istanza a parte.
               #otterremo una lista di tuple in cui il primo valore è corso mentre il secondo il count
               ris.append( (Corso(row["codins"],
                                  row["crediti"],
                                  row["nome"],
                                  row["pd"]    ),
                            row["n"] ))
           cursor.close()
           cnx.close()
           return ris
               #se dimentichi il return python restituisce None

    # ----------------------------------------------------------------------------------------------------------------------------
   @staticmethod
   def getStudentiPerCorso(codins):

       cnx= DBConnect.get_connection()
       ris = []
       if cnx is None:
           print("Connessione fallita")
           return ris
       else:
           cursor = cnx.cursor(dictionary=True)
           query= """select s.*
                     from studente s, iscrizione i
                     where s.matricola = i.matricola
                     and i.codins = %s """
           cursor.execute(query, (codins,))

           for row in cursor:
               ris.append( Studente(**row))
               # ris.append(Studente(row["matricola"],
               #                     row["cognome"],
               #                     row["nome"],
               #                     row["CDS"]))

           cursor.close()
           cnx.close()
           return ris

   # ----------------------------------------------------------------------------------------------------------------------------
   @staticmethod
   def getCDSperCorso(codins):

       cnx= DBConnect.get_connection()
       ris = []
       if cnx is None:
           print("Connessione fallita")
           return ris
       else:
           cursor= cnx.cursor(dictionary=True)
           query= """ select s.CDS, count(*) as n
                      from studente s, iscrizione i
                      where s.matricola = i.matricola
                      and i.codins = %s
                      and s.CDS != ""
                      group by s.CDS
                        """
           cursor.execute(query, (codins,))

           for row in cursor:
               ris.append( (row["CDS"],
                             row["n"] )
                           )
           cursor.close()
           cnx.close()
           return ris


#voglio leggere se la query è giusta, poi oggetto giusto
if __name__ == '__main__':
    print(DAO.getCodins())
    print(DAO.getAllCorsi( ))

if __name__ == "__main__":
    for c in DAO.getCorsiPDwithIscritti(1):
        print(c)

if __name__ == "__main__":
    for c in DAO.getCDSperCorso("02PBVPG"):
        print(c)
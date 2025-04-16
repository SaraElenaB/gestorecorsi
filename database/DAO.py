from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente


class DAO(): #def init non serve nel DAO

   #----------------------------------------------------------------------------------------------------------------------------
   @staticmethod
   def getCodins():
       cnx= DBConnect.get_connection()
       cursor = cnx.cursor(dictionary=True)
       query= """select c.codins
                from corso c """
       cursor.execute(query)

       ris = []
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
       cursor = cnx.cursor(dictionary=True)
       query = """select *
                   from corso c """
       cursor.execute(query)

       ris = []
       for row in cursor:
           #ris.append( Corso( codins=row["codins"], crediti=row["crediti"], nome=row["nome"], pd=row["pd"] ))
           #voglio l'oggetto Corso --> importo, e poi codins è uguale all'oggetto del ciclo da cui prendo uno specifico campo dato che row è un dizionario

           ris.append( Corso(**row))
       cursor.close()
       cnx.close()
       return ris

    #----------------------------------------------------------------------------------------------------------------------------
   @staticmethod
   def getCorsi():
       cnx= DBConnect.get_connection()
       cursor = cnx.cursor(dictionary=True)
       query= """select c.codins
                from corso c """
       cursor.execute(query)

       ris = []
       for row in cursor:
           ris.append(row["codins"]) #altirmenti senza dict=True sarebbe una tupla
                                     # e quindi devo prendere il primo elemento devi fare row[0]

       cursor.close()
       cnx.close()
       return ris

#voglio leggere se la query è giusta, poi oggetto giusto
if __name__ == '__main__':
    print(DAO.getCodins())
    print(DAO.getAllCorsi( ))
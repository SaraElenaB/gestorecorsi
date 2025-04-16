from dataclasses import dataclass
#from model.studente import Studente

#crei tu
@dataclass
class Corso:
    codins: str
    crediti: int
    nome: str
    pd: int

    #studenti: list[Studente]= None #lazy initialization
    matricole: list[str] = None

    #per dare senso al dataclass definisci eq e hash
    def __eq__(self, other):
        # quando due oggetti corso sono uguali?
        return self.codins == other.codins

    def __hash__(self):
        #se vuoi mappare, quale chiave primaria devi prendere
        return hash(self.codins)

    def __str__(self):
        return f"{self.nome} ({self.codins}) - {self.crediti} CFU"

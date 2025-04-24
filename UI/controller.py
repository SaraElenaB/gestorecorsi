import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        #aggiunto io:
        self._ddCodinsValue= None #cosi mi si salva in automatico

    #----------------------------------------------------------------------------------------------------------------------
    def fillddCodins(self):

        listaCodins = self._model.getAllCorsi()

        #OGGETTO:
        for c in listaCodins:
            self._view.ddCodins.options.append( ft.dropdown.Option( key= c.codins,
                                                                    data=c,
                                                                    on_click=self._choiceDDCodins
                                                                    ))

        #STRINGA:
        # listaCodins = self._model.getCorsi()
        # for cod in listaCodins:
        #       #essendo un dropdown devo fare options --> ft.dropdown.Option(cod)
        #       #devo aggiungere oggetti di tipo option non qualsiasi
        #     self._view.ddCodins.options.append( ft.dropdown.Option(cod))
        return

    # ----------------------------------------------------------------------------------------------------------------------
    def _choiceDDCodins(self, e):
        #serve per salvare in una variabile l'oggetto corso che abbiamo preso dalla sezione
        self._ddCodinsValue= e.control.data #riesco a controllare l'oggetto nel dropdown

    #----------------------------------------------------------------------------------------------------------------------
    def handlePrintCorsiPD(self, e):

        self._view.lvTxtOut.controls.clear()
        pd= self._view.ddPeriodoDidattico.value

        if pd is None:
            #1° modo:
            # self._view.lvTxtOut.controls.append( ft.Text("Attenzione selezionare un periodo didattico!", color="red"))
            # self._view.update_page()
            #return

            #2° modo:
            self._view.create_alert("Attenzione, selezionare un periodo didattivo!")
            self._view.update_page()
            return
        else:

            #a questo punto pd="I" o "II" ma noi vogliamo i numero
            if pd=="I":
                pdInt=1
            else:
                pdInt=2

            corsiPD = self._model.getCorsiPD(pdInt)
            #nel caso sia vuoto
            if len(corsiPD) == 0:
                self._view.lvTxtOut.controls.append( ft.Text( "Nessun corso trovato in questo periodo! "))
                self._view.update_page()
                return

            self._view.lvTxtOut.controls.append( ft.Text( f"Corsi periodo didattico {pd}: "))
            for c in corsiPD:
                self._view.lvTxtOut.controls.append( ft.Text(c))
            self._view.update_page()

    # ----------------------------------------------------------------------------------------------------------------------
    def handlePrintIscrittiCorsiPD(self, e):

        self._view.lvTxtOut.controls.clear()
        pd = self._view.ddPeriodoDidattico.value
        if pd is None:
            self._view.create_alert("Attenzione, selezionare un periodo didattico!")
            self._view.update_page()
            return

        if pd=="I":
            pdInt=1
        else:
            pdInt=2

        corsiPDwithIscritti = self._model.getCorsiPDwithIscritti(pdInt)
        if len(corsiPDwithIscritti) == 0:
            self._view.lvTxtOut.controls.append(ft.Text("Nessun corso trovato in questo periodo! "))
            self._view.update_page()
            return

        self._view.lvTxtOut.controls.append( ft.Text( f"Dettagli corsi del {pd} periodi didattico: "))
        for c in corsiPDwithIscritti:
            #c è una TUPLA
            self._view.lvTxtOut.controls.append( ft.Text( f"{c[0]} - Numero iscritti: {c[1]} "))

        self._view.update_page()

    # ----------------------------------------------------------------------------------------------------------------------
    def handlePrintIscrittiCodins(self, e):

        self._view.lvTxtOut.controls.clear()
        codins = self._view.ddCodins.value
        if codins is None:
            self._view.create_alert("Attenzione, selezionare un codice corso!")
            self._view.update_page()
            return

        studentiPerCorso = self._model.getStudentiPerCorso(codins)
        if len(studentiPerCorso) == 0:
            self._view.lvTxtOut.controls.append(ft.Text("Nessun studente trovato in questo corso! "))
            self._view.update_page()
            return

        self._view.lvTxtOut.controls.append( ft.Text( f"Dettagli studenti del corso {codins}: "))
        for c in studentiPerCorso:
            self._view.lvTxtOut.controls.append( ft.Text(c))

        self._view.update_page()

        #metodo 1 --> stringa con solo codice
                     #come ho eseguito qui sopra

        #metodo 2 --> oggetto corso
                     # il codice in realtà già lo avevi dal metodo
                     # salvo nel costruttore il ddCodinsValue=None
                     # -- if self._ddCodinsValue is None (uguale)
                     # -- studentiPerCorso = self._model.getStudentiPerCorso( self._ddCodinsValue.codins)
                     # -- ft.Text( f"Studenti iscritti al corso {self._ddCodinsValue.nome}

    # ----------------------------------------------------------------------------------------------------------------------
    def handlePrintCDSCodins(self, e):

        self._view.lvTxtOut.controls.clear()
        #uso l'oggetto
        if self._ddCodinsValue is None:
            self._view.create_alert("Attenzione, selezionare un corso!")
            self._view.update_page()
            return

        cds= self._model.getCDSperCorso(self._ddCodinsValue.codins)
        if len(cds) == 0:
            self._view.lvTxtOut.controls.append(ft.Text("Nessun Corso Di Studio trovato in questo corso! "))
            self._view.update_page()
            return
        for c in cds:
            self._view.lvTxtOut.controls.append( ft.Text( f" Corso di Studio {c[0]} - Numero iscritti: {c[1]} "))

        self._view.update_page()


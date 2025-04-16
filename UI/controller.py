import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

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
        pass

    # ----------------------------------------------------------------------------------------------------------------------
    def handlePrintIscrittiCorsiPD(self, e):
        pass

    # ----------------------------------------------------------------------------------------------------------------------
    def handlePrintIscrittiCodins(self, e):
        pass

    # ----------------------------------------------------------------------------------------------------------------------
    def handlePrintCDSCodins(self, e):
        pass



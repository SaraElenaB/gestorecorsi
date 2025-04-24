import flet as ft

class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Gestore Corsi edizione 2025"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None

        # graphical elements --> lo facciamo solo perchè cosi sappiamo cosa c'è nel database
        self._title = None
        self.ddPeriodoDidattico= None #dd=Dropdown
        self.ddCodins= None #codice di insegnamento lo prendiamo da un dropdown non da testo, cosi non dobbiamo controllare se è corretto
        self.btnPrintCorsiPD= None
        self.btnPrintIscrittiCorsiPD= None
        self.btnPrintIscrittiCodins= None
        self.btnPrintCDSCodins= None
        self.lvTxtOut= None


    #-------------------------------------------------------------------------------------------------------------------------------
    def load_interface(self):
        # title
        self._title = ft.Text("Gestore Corsi", color="blue", size=24)

        #row1
        self.ddPeriodoDidattico= ft.Dropdown( label="Periodo Didattico", width=200,
                                              expand=True,
                                              options=[
                                                  ft.dropdown.Option("I"),
                                                  ft.dropdown.Option("II") ]
                                              )
                                              # solo perchè già sappiamo che ci sono queste due opzioni
                                              # spesso --> leggere questa info dal database

        self.btnPrintCorsiPD = ft.ElevatedButton( text="Stampa corsi", width=300,
                                                  on_click=self._controller.handlePrintCorsiPD)
        self.btnPrintIscrittiCorsiPD =ft.ElevatedButton( text="Stampa iscitti", width=300,
                                                         on_click=self._controller.handlePrintIscrittiCorsiPD)
        row1= ft.Row( [self.ddPeriodoDidattico, self.btnPrintCorsiPD, self.btnPrintIscrittiCorsiPD], alignment=ft.MainAxisAlignment.CENTER)

        #row2
        self.ddCodins = ft.Dropdown( label="Corso", width=200, expand = True)

            #PROBLEMA: noi abbiamo implementato questo metodo inserendo l'oggetto corso ma quando prendiamo il value lo vede come una stringa
            # quindi dobbiamo fare questi passaggi:
            #        1. on_change --> in quanto viene chiamato quando facciamo una selezione
            #        2. def _choiceDDCodins(self, e) --> in controller ma viene chiamato dall'operazione presente nel controller che ha l'option di dropdown
        self._controller.fillddCodins() #caso in cui non le so e le devo prendere dal database
                                        #view--> controller--> model--> DAO--> query: database

        self.btnPrintIscrittiCodins = ft.ElevatedButton( text="Stampa iscritti al corso", width=300,
                                                  on_click=self._controller.handlePrintIscrittiCodins)
        self.btnPrintCDSCodins= ft.ElevatedButton( text="Stampa CDS per il corso", width=300,
                                                  on_click=self._controller.handlePrintCDSCodins)
        row2= ft.Row( [self.ddCodins, self.btnPrintIscrittiCodins, self.btnPrintCDSCodins], alignment=ft.MainAxisAlignment.CENTER)

        #Output
        self.lvTxtOut= ft.ListView(expand=True)

        #Visualizzare
        self._page.add(self._title, row1, row2, self.lvTxtOut)
        self._page.update()

    # -------------------------------------------------------------------------------------------------------------------------------
    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    # -------------------------------------------------------------------------------------------------------------------------------
    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    # -------------------------------------------------------------------------------------------------------------------------------
    def update_page(self):
        self._page.update()

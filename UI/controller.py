import flet as ft
from UI.view import View
from model.model import Autonoleggio
from model.automobile import Automobile

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view : View, model : Autonoleggio):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO
    def mostra_automobili(self,e):
        if self._view.page:
            self.lista = ft.ListView(expand=True)

            lista2 = self._model.get_automobili()
            for macchina in lista2:
                self.lista.controls.append(ft.Text(macchina))
            self._view.page.add(self.lista)

        else:
            None
    def cerca_automobili(self,e):
        modello = self._view.testoRicerca.value
        lista=self._model.cerca_automobili_per_modello(modello)
        print(lista)
        lista_modello_view=ft.ListView(expand=True)
        for macchine in lista:
            lista_modello_view.controls.append(ft.Text(macchine))
        self._view.page.add(lista_modello_view)
        self._view.page.update()




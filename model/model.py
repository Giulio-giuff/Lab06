from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile
        self.lista_auto = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """
        # TODO
        tabella = []
        cnx=get_connection()
        cursor=cnx.cursor()
        cursor.execute('SELECT * FROM automobile')
        tabella=cursor.fetchall()
        for riga in tabella:
            macchina=Automobile(*riga)
            self.lista_auto.append(macchina)
        return self.lista_auto

    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        # TODO
        lista_modello=[]
        self.lista_auto=self.get_automobili()
        for macchine in self.lista_auto:
            if str(macchine.modello) == str(modello):
                lista_modello.append(macchine)
        return lista_modello



from tkinter import *

class Soma:
    def _init__(self):
        self.tela = Tk()
        self.configura_tela()
        self.criar_componentes()
        self.calcula()
        
        #atributos privados
        self.__num1 = int
        self.__num2 = int
        self.__soma = int
        
    @property
    def _num1(self):
        return self.__num1
    @_num1.setter
    def _num1(self, value):
        self.__num1 = value
        
    @property
    def _num2(self):
        return self.__num2
    @_num2.setter
    def _num2(self, value):
        self.__num2 = value
        
    @property
    def _soma(self):
        return self.__soma
    @_soma.setter
    def _soma(self, value):
        self.__soma = value
        
    def configura_tela(self):
        self.tela.title("Soma de dois números")
        
        #commitar e terminar na faculdade
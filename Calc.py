'''
Created on Mar 16, 2024

@author: TheGr
'''
from math import *
class Calculadora:
    def __init__(self, primerNum = 0, segundoNum = 1, operacion="+"):
        self.primerNumero = float(primerNum)
        self.operador = operacion
        self.segundoNumero = float(segundoNum)
        self.enMemoria = 0
        
        self.nuevoOperador = False
        self.nuevoNumero = False
        self.recorrido = False
        self.resultao = False
        
    def Mmenos(self, n):
        self.enMemoria -= float(n)
    def Mmas(self, n):
        self.enMemoria += float(n)
    def MS(self, n):
        self.enMemoria = float(n)
    def MR(self):
        return self.enMemoria
    def MC(self):
        self.enMemoria = 0
    def CE(self):
        self.segundoNumero = 0
    def C(self):
        self.primerNumero = 0
        self.segundoNumero = 0
        self.operador = "+"
        
        self.recorrido = False
        self.nuevoNumero = False
        self.nuevoOperador = False
    
    def agregarNumero(self, num):
        self.nuevoNumero = True
        if(self.nuevoOperador):
            self.primerNumero = self.segundoNumero
            self.recorrido = True
        self.segundoNumero = num
        print(str(self.primerNumero), str(self.segundoNumero))
        
    def agregarOperador(self, op):
        print("operador: " + op)
        #operacion automatica si hay numero despues de operador
        if(not self.recorrido):
            pass
        elif(self.nuevoNumero and self.nuevoOperador):
            print("catchup")
            nuevoSeg = self.identificar()
            self.primerNumero = self.segundoNumero
            self.segundoNumero = nuevoSeg
            
        self.operador = op
    def operadorEstado(self):
        self.nuevoNumero = False
        self.nuevoOperador = True
    #casos ordinarios
    def sumar(self):
        return float(self.primerNumero) + float(self.segundoNumero)
    def restar(self):
        return float(self.primerNumero) - float(self.segundoNumero)
    def multiplicar(self):
        return float(self.primerNumero) * float(self.segundoNumero)
    def dividir(self):
        return float(self.primerNumero) / float(self.segundoNumero)
    
    #caso multiproposito
    def porcentaje(self, num):
        return float(num)/100
    
    def modulo(self):
        if(self.operador == "+" or self.operador == "-"):
            self.segundoNumero = float(self.primerNumero)*self.porcentaje(self.segundoNumero)
        if(self.operador == "*" or self.operador == "/"):
            self.segundoNumero = self.porcentaje(self.segundoNumero)
        
        print("mod res ", str(self.primerNumero), str(self.segundoNumero))
    #casos especiales
    def cuadrado(self, n):
        return float(n) * float(n)
    def raiz(self, n):
        if(float(n) < 0): return -sqrt(abs(float(n)))
        return sqrt(abs(float(n)))
    def bajoUno(self, n):
        return 1/float(n)
    
    def identificar(self):
        self.resultao = True
        self.recorrido = False
        print("ident: " + self.operador)
        if(self.operador == "+"):
            print(str(self.primerNumero) + " " + str(self.segundoNumero))
            return self.sumar()
        if(self.operador == "-"):
            return self.restar()
        if(self.operador == "*"):
            return self.multiplicar()
        if(self.operador == "/"):
            return self.dividir()
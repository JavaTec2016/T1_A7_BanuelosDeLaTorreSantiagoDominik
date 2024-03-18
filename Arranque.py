'''
Created on Mar 16, 2024

@author: TheGr
'''
from tkinter import *
import tkinter as tk
from tkinter import messagebox as mg

from Calc import *

ventana_inicio = Tk()
ventana_inicio.title("GUI con PYTHON")
ventana_inicio.geometry("320x630")

calculadora = Calculadora()

contexto = StringVar()
numeros = StringVar()

def checarPuntos(txt=""):
    ap=0
    for i in txt:
        if(i=="." and ap!=0): return False
        ap += 1 
    return True

#actualiza a la calculadora, primero el numero y luego el operador
#agregar un operador a veces hace operaciones rezagadas
def establecerOperador(op):
    calculadora.resultao = False
    print("operador establecido: " + op)
    calculadora.agregarNumero(numeros.get())
    calculadora.agregarOperador(op)
    if(calculadora.nuevoNumero and calculadora.nuevoOperador):
        numeros.set(calculadora.segundoNumero)
    calculadora.operadorEstado()
    
    establecerContexto(str(calculadora.segundoNumero)+" "+calculadora.operador)
    
#captura el numero a modular, a veces trabaja respecto a ambos operandos
#actualiza la pantalla al terminar
def modular():
    print("modulando")
    calculadora.resultao = False
    numb = calculadora.segundoNumero
    calculadora.agregarNumero(numeros.get())
    
    calculadora.modulo()
    establecerContexto(contexto.get()+"  "+str(calculadora.segundoNumero))
    numeros.set(calculadora.segundoNumero)
    
    calculadora.agregarNumero(0)
    calculadora.agregarNumero(numb)
    
    
    
def invertir():
    calculadora.resultao = False
    establecerContexto("-("+str(numeros.get())+")")
    numeros.set(-float(numeros.get()))

def operadorEspecial(op):
    calculadora.resultao = False
    if(op == "sqrt"):
        establecerContexto("raiz("+str(numeros.get())+")")
        numeros.set(calculadora.raiz(numeros.get()))
        
    elif(op == "x^2"):
        establecerContexto("("+str(numeros.get())+")^2")
        numeros.set(calculadora.cuadrado(numeros.get()))
        
    elif(op == "1/x"):
        establecerContexto("1/("+str(numeros.get())+")")
        numeros.set(calculadora.bajoUno(numeros.get()))
        

#muestra un numero, a veces borra el anterior
def mostrarNumero(num):
    print("numero establecido: " + num)
    if((calculadora.nuevoOperador and (not calculadora.nuevoNumero)) or calculadora.resultao):
        numeros.set("")
    numeros.set(numeros.get() + str(num))
    calculadora.nuevoNumero = True
    calculadora.resultao = False

def igual(num):
    calculadora.agregarNumero(num)
    establecerContexto(str(calculadora.primerNumero)+" "+calculadora.operador+" "+str(calculadora.segundoNumero)+" =")
    
    numeros.set(str(calculadora.identificar()))
    calculadora.agregarNumero(numeros.get())
    calculadora.agregarNumero(0)    
    calculadora.nuevoOperador = False

def punto():
    calculadora.resultao = False
    if(checarPuntos(numeros.get())): mostrarNumero(".")

def establecerContexto(t):
    contexto.set(t)

def CE():
    calculadora.resultao = True
    calculadora.CE()
    numeros.set(0)
def C():
    calculadora.resultao = True
    calculadora.C()
    numeros.set(0)
def MR():
    calculadora.resultao = True
    numeros.set(calculadora.MR())
def MS():
    calculadora.resultao = True
    calculadora.MS(numeros.get())

caja_contexto = Entry(ventana_inicio, bg="lightgray",
                         fg="black", font=("roboto", 10, "bold"),
                         width=21, justify=tk.RIGHT, textvariable=contexto)
caja_contexto.grid(row=0,column=0, columnspan=30)

caja_operaciones = Entry(ventana_inicio, bg="cyan",
                         fg="white", font=("roboto", 20, "bold"),
                         width=21, justify=tk.RIGHT, textvariable=numeros)
caja_operaciones.grid(row=1,column=0, columnspan=30)

#botones de memoria

btnMC = Button(ventana_inicio, bg="gray", fg="black", text="MC", width=6, height=3,
                command=lambda:calculadora.MC())
btnMC.grid(row=2, column=0*2, columnspan=2)

btnMR = Button(ventana_inicio, bg="gray", fg="black", text="MR", width=6, height=3,
                command=lambda:MR())
btnMR.grid(row=2, column=1*2, columnspan=2)

btnMmas = Button(ventana_inicio, bg="gray", fg="black", text="M+", width=6, height=3,
                command=lambda:calculadora.Mmas(numeros.get()))
btnMmas.grid(row=2, column=2*2, columnspan=2)

btnMmenos = Button(ventana_inicio, bg="gray", fg="black", text="M-", width=6, height=3,
                command=lambda:calculadora.Mmenos(numeros.get()))
btnMmenos.grid(row=2, column=3*2, columnspan=2)

btnMS = Button(ventana_inicio, bg="gray", fg="black", text="MS", width=6, height=3,
                command=lambda:MS())
btnMS.grid(row=2, column=4*2, columnspan=2)

btnMx = Button(ventana_inicio, bg="gray", fg="black", text="M~", width=6, height=3)
btnMx.grid(row=2, column=5*2, columnspan=2)

btnMod = Button(ventana_inicio, bg="gray", fg="black", text="%", width=10, height=5,
                command=lambda:modular())
btnMod.grid(row=3, column=0*3, columnspan=3)

btnCE = Button(ventana_inicio, text="CE", width=10, height=5, bg="gray", fg="black",
               command=lambda:CE())
btnCE.grid(row=3, column=1*3, columnspan=3)

btnC = Button(ventana_inicio, text="C", width=10, height=5, bg="gray", fg="black",
              command=lambda:C())
btnC.grid(row=3, column=2*3, columnspan=3)

btnBorrar = Button(ventana_inicio, text="DEL", width=10, height=5, bg="gray", fg="black",
                   command=lambda:numeros.set(numeros.get()[:-1]))
btnBorrar.grid(row=3, column=3*3, columnspan=3)


btnBajoUno = Button(ventana_inicio, text="1/x", width=10, height=5, bg="gray", fg="black",
                    command=lambda:operadorEspecial("1/x"))
btnBajoUno.grid(row=5, column=0*3, columnspan=3)

btnCuadrado = Button(ventana_inicio, text="x^2", width=10, height=5, bg="gray", fg="black",
                     command=lambda:operadorEspecial("x^2"))
btnCuadrado.grid(row=5, column=1*3, columnspan=3)

btnSqrt = Button(ventana_inicio, text="sqrt", width=10, height=5, bg="gray", fg="black",
                command=lambda:operadorEspecial("sqrt"))
btnSqrt.grid(row=5, column=2*3, columnspan=3)

btnDiv = Button(ventana_inicio, text="/", width=10, height=5, bg="gray", fg="black",
                command=lambda:establecerOperador("/"))
btnDiv.grid(row=5, column=3*3, columnspan=3)

btn7 = Button(ventana_inicio, text="7", width=10, height=5, bg="gray", fg="black",
               command=lambda:mostrarNumero("7"))
btn7.grid(row=6, column=0*3, columnspan=3)

btn8 = Button(ventana_inicio, text="8", width=10, height=5, bg="gray", fg="black",
               command=lambda:mostrarNumero("8"))
btn8.grid(row=6, column=1*3, columnspan=3)

btn9 = Button(ventana_inicio, text="9", width=10, height=5, bg="gray", fg="black",
               command=lambda:mostrarNumero("9"))
btn9.grid(row=6, column=2*3, columnspan=3)

btnMult = Button(ventana_inicio, text="x", width=10, height=5, bg="gray", fg="black",
                 command=lambda:establecerOperador("*"))
btnMult.grid(row=6, column=3*3, columnspan=3)

btn4 = Button(ventana_inicio, text="4", width=10, height=5, bg="gray", fg="black",
               command=lambda:mostrarNumero("4"))
btn4.grid(row=7, column=0*3, columnspan=3)

btn5 = Button(ventana_inicio, text="5", width=10, height=5, bg="gray", fg="black",
               command=lambda:mostrarNumero("5"))
btn5.grid(row=7, column=1*3, columnspan=3)

btn6 = Button(ventana_inicio, text="6", width=10, height=5, bg="gray", fg="black",
               command=lambda:mostrarNumero("6"))
btn6.grid(row=7, column=2*3, columnspan=3)

btnMenos = Button(ventana_inicio, text="-", width=10, height=5, bg="gray", fg="black",
                  command=lambda:establecerOperador("-"))
btnMenos.grid(row=7, column=3*3, columnspan=3)

btn1 = Button(ventana_inicio, text="1", width=10, height=5, bg="gray", fg="black",
               command=lambda:mostrarNumero("1"))
btn1.grid(row=8, column=0*3, columnspan=3)

btn2 = Button(ventana_inicio, text="2", width=10, height=5, bg="gray", fg="black",
               command=lambda:mostrarNumero("2"))
btn2.grid(row=8, column=1*3, columnspan=3)

btn3 = Button(ventana_inicio, text="3", width=10, height=5, bg="gray", fg="black",
               command=lambda:mostrarNumero("3"))
btn3.grid(row=8, column=2*3, columnspan=3)

btnSuma = Button(ventana_inicio, text="+", width=10, height=5,bg="gray", fg="black",
                 command=lambda:establecerOperador("+"))
btnSuma.grid(row=8, column=3*3, columnspan=3)

btnInvertir = Button(ventana_inicio, text="+/-", width=10, height=5,bg="gray", fg="black",
               command=lambda:invertir())
btnInvertir.grid(row=10, column=0*3, columnspan=3)

btn0 = Button(ventana_inicio, text="0", width=10, height=5,bg="gray", fg="black",
               command=lambda:mostrarNumero("0"))
btn0.grid(row=10, column=1*3, columnspan=3)

btnPunto = Button(ventana_inicio, text=".", width=10, height=5,bg="gray", fg="black",
               command=lambda:punto())
btnPunto.grid(row=10, column=2*3, columnspan=3)

btnRes = Button(ventana_inicio, text="=", width=10, height=5,bg="gray", fg="black",
                command=lambda:igual(numeros.get()))
btnRes.grid(row=10, column=3*3, columnspan=3)

ventana_inicio.mainloop()
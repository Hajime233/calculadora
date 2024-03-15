from MainFrame.mainframe import *
import math


#-- Logica--
 #--- Data entry---

def datos(dato, Ecuacion, Resultado):
    if dato.isdigit() or dato in ['(', ')', '.']:
        Ecuacion.set(Ecuacion.get() + dato)
    elif dato in ['*', '/', '+', '-']:
        ecuacion_actual = Ecuacion.get()
        if ecuacion_actual:
            try:
                total = eval(ecuacion_actual)
                Ecuacion.set(str(total) + dato)
                Resultado.set(str(total))
            except Exception as e:
                Resultado.set('Error')
    elif dato == '=':
        ecuacion_actual = Ecuacion.get()
        if ecuacion_actual:
            try:
                total = eval(ecuacion_actual)
                Resultado.set(str(total))
            except Exception as e:
                Resultado.set('Error')
        else:
            Resultado.set('')


def raizcuadrada(Ecuacion, Resultado):
    try:
        numero = float(Ecuacion.get())
        resultado_raiz = math.sqrt(numero)
        Resultado.set(str(resultado_raiz))
    except ValueError:
        Resultado.set('Error')

def borrar(Ecuacion):
    ecuacion_actual = Ecuacion.get()
    if ecuacion_actual:
        nueva_ecuacion = ecuacion_actual[:-1]
        Ecuacion.set(nueva_ecuacion)



def limpiar(Resultado,Ecuacion):
    Ecuacion.set('')
    Resultado.set('')
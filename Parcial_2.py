###################################################################
#se importan los paquetes necesarios para el desarrollo del codigo#
###################################################################
import numpy as np
import sys
from numpy.polynomial.polynomial import Polynomial
import random as rd
##################################################################
#se definen los textos que van a ser usados a lo largo del codigo#
##################################################################
txt1="Ingrese el grado del polinomio: "
txt2="El número no es valido, asegurese de que sea un natural: "
txt3="Ingrese los valores de los coeficientes en orden: "
txt4="Ingrese un valor de x_n para aproximar las raices: "
txt5="-Las raices del polinomio son:"
txt6="-El polinomio ingresado es: "
txt7="-La raíz del polinomio es: "
txt8="-Las aproximaciones de una de las raices del polinomio son: "
#########################################################
#se solicita el grado del polinomio a traves del teclado#
#########################################################
n=eval(input(txt1))
N=n+1
#############################################
#filtro para la entrada de datos por teclado#
#############################################
if N!=int(N):
    
    sys.exit(txt2)
if N<0:
    
    sys.exit(txt2)
######################################################
#se define la lista A, esta contiene los coeficientes#
######################################################
A=[]
####################################################
#se pide el ingreso de los coeficientes por teclado#
####################################################
for y in range(N):
    valor=int(input(txt3))
    A.append(valor)
######################################################################
#se crea otra lista con los coeficientes de la derivada del polinomio#
######################################################################
d=list(range(0,N))
d1=np.multiply(A,d)
d2=d1[1:]#se elimina el termino constante
d_in=sorted(d2,reverse=True)
A_in=sorted(A,reverse=True)
##################################################
#se expresan las dos listas en formato polinomial#
##################################################
funcion=Polynomial(A)
funcion_derivada=Polynomial(d2)
###########################################################
#Definimos un x_n para hacer la aproximación de las raices#
###########################################################
x_n=rd.randint(-10,10)
#x_n=eval(input(txt4))
###############################################################
#si desea elegir un x_n arbitrario comente la linea 51 y borre#
#el comentario de la linea 52                                 #     
###############################################################
##########################################################
#se crea una lista pñara almacenar las raices aproximadas#
##########################################################
aproximaciones=[]
#####################################################
#por medio de un ciclo se hacen las 4 aproximaciones#
#####################################################
for k in range (4):
    f_1=np.polyval(A_in,x_n)
    f_2=np.polyval(d_in,x_n)
    x=x_n-(f_1/f_2)
    aproximaciones.append([x])
    Raices=(np.roots(A_in)).real
    #############################################################
    #se hace un condicional para frenar el ciclo si se consigue-#
    #la raiz exacta antes de los 4 intentos                     #
    #############################################################
    x_n=x
    if x in Raices:
        break
aproximaciones= np.array(aproximaciones)
############################################################
#se uso la funcion array para que la salida se vea ordenada#
############################################################
print(txt6)
print(funcion)#muestra el polinomio
print(txt5)
print(Raices)#muestra las raices reales dadas por la herramienta roots
#################################################################
#se plantean los casos posibles en los que se encuentra         #   
#la raiz exacta con el metodo o solo se llega a 4 aproximaciones#
#################################################################
if len(aproximaciones)==1:
    print(txt7)
else:
    print(txt8)
print(aproximaciones)#muestra las aproximaciones obtenidas





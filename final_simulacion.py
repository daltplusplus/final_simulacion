import random
import math
import time
from datetime import datetime, timedelta

#variables de estado
ST1 = 0
ST2 = 0
ST3 = 0

#datos
VD1 = 0
VD2 = 0
VD3 = 0
DP = 0
CVL = 0

#variables de control
TP = 30000
DL = 50 #poner como porcentaje ejemplo: 50 en lugar de 0.5
STR = 2000

#auxiliares
T = 0
PRECIO1 = 1196500
PRECIO2 = PRECIO1 * 0.70
PRECIO3 = PRECIO2 * 0.70
FV = 1.0
FP = 1.0
BEN = 0
LIQ = 0
DES = 0
TOT = 0
VDT = 0
diasEspeciales = [5,167,359] #dias en los que las ventas suben un porcentaje fijo

#TEF
FLL = 1

def main():
    global T, FLL, ST1, VD1, ST2, STR
    while T < 356* 10:
        T += 1
        
        determinar_fecha_especial()

        if T == FLL:
            reponer()

        calcular_ventas_diarias()

        if ST1 < STR and FLL < T:
            realizar_pedido()

        if T % 365 == 0:
            cerrar_anio()
    
    imprimir_resultados()


def determinar_fecha_especial():
    global T, diasEspeciales, FP, FV, DL
    FP = 1.0
    FV = 1.0
    for k in diasEspeciales:
        if T % 365 == k - 365:
            FV = 1.2
    
    if T % 365 == 0:
        FP = DL
        FV = (0.5* DL*DL +1.8 *DL - 1.18)/100
            
        
def imprimir_resultados():
    print("BA = " + str(BEN*365/T))
    print("LT = " + str(LIQ/TOT))
    print("PLA = " + str(LIQ*365/T))
    print("PDA = " + str(DES*365/T))
    print("ST1 = " + str(ST1))
    print("ST2 = " + str(ST2))
    print("ST3 = " + str(ST3))

def cerrar_anio():
    global LIQ, VDT, DES, ST1, ST2, ST3
    LIQ += VDT
    DES += ST3
    ST3 = ST2
    ST2 = ST1
    ST1 = 0

def realizar_pedido():
    global DP, FLL, T
    DP = random.randint(2,5)
    FLL = T + DP

def calcular_ventas_diarias():
    global VD1, VD2, VD3, ST1, ST2,ST3, VDT, BEN

    VD1 = random.randint(200, 700)
    VD2 = random.randint(40, 140)
    VD3 = random.randint(8, 28)

    VDT = 0

    BEN += min(ST1, VD1*FV)* PRECIO1 * FP
    VDT += min(ST1, VD1*FV) 
    ST1 = max(ST1-VD1*FV, 0)

    BEN += min(ST2, VD2*FV)* PRECIO2 * FP
    VDT += min(ST2, VD2*FV) 
    ST2 = max(ST2-VD2*FV, 0)

    BEN += min(ST3, VD3*FV)* PRECIO3 * FP
    VDT += min(ST3, VD3*FV) 
    ST3 = max(ST3-VD3*FV, 0)


def restar_stock(stock, ventas, precio):
    global BEN, VDT
    if  stock < ventas*FV:
        BEN += stock * FV * precio * FP
        stock = 0
        VDT

def reponer():
    global ST1, TOT, FLL
    ST1 += TP
    TOT += TP
    FLL = 0

main()

#observaciones
#no se desechan celulares a menos que las reposiciones sean ridiculamente grandes
#posible solucion 1: incluir reposicion de celulares viejos

#el sistema no tiene nocion de las ventas perdidas por falta de stock
#posible solucion 1: incluir un resultado que contemple las ventas perdidas
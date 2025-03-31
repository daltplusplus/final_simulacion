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
DL = 20
STR = 2000

#auxiliares
T = 0
PRECIO1 = 1196500
PRECIO2 = PRECIO1 * 0.70
PRECIO3 = PRECIO2 * 0.70
FV = 1
FP = 1
BEN = 0
LIQ = 0
DES = 0
TOT = 0
VDT = 0

#TEF
FLL = 1

def main():
    global T, FLL, ST1, VD1, ST2, STR
    while T < 356* 10:
        T += 1
        
        if T == FLL:
            reponer()

        calcular_ventas_diarias()

        if ST1 < STR and FLL < T:
            realizar_pedido()

        if T % 365 == 0:
            cerrar_anio()
    
    imprimir_resultados()

        
def imprimir_resultados():
    print("BA = " + str(BEN*365/T))
    print("L = " + str(LIQ))
    print("T = " + str(TOT))
    print("LT = " + str(LIQ/TOT))
    print("PLA = " + str(LIQ*365/T))
    print("PDA = " + str(DES*365/T))

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
    VD2 = random.randint(100, 350)
    VD3 = random.randint(30, 100)

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
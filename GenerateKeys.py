__author__ = 'Julian'

import random

def bin(decimal):
    entero = int(decimal)
    binario=''
    while entero != 0:
        residuo = entero % 2
        entero = int(entero / 2)
        binario = str(residuo) + binario
    return binario

# a^b mod n
def powerMod(a, b, n):
    bbin = bin(b)
    z = a
    for i in range(1,len(bbin)):
        digit = bbin[i]
        if digit == '1':
            z = ((z**2)*a) % n
        else:
            z = (z**2) % n
    return z


def EEA(a, b):
    aCol = []
    bCol = []
    aCol.append(a)
    bCol.append(b)
    while b != 0:
        temp = b
        b = a % b
        a = temp
        aCol.append(a)
        bCol.append(b)
    x = 1
    y = 0
    mcd = int(aCol[len(aCol)-1])
    for i in range(0, len(aCol)-1):
        x = y
        y = int((mcd-(int(aCol[len(aCol)-i-2])*x))/int(bCol[len(bCol)-i-2]))
    return x, y


def keyGenerator(p, q):
    publicKey=[]
    privateKey = []
    n = p*q
    phi = (p-1)*(q-1)
    e = 79
    c, d = EEA(phi, e)

    publicKey.append(e)
    publicKey.append(n)

    privateKey.append(d)
    privateKey.append(n)
    return publicKey, privateKey


def generateE(phi):
    salir = True
    while salir:
        e = random.randint(1, phi-1)
        if mcd(e, phi) == 1:
            salir = False
    return e

def mcd(a, b):
    if b == 0:
        return a
    return mcd(b, a % b)



__author__ = 'estma_000'

import GenerateKeys
import Primos
import random


m = input("Ingrese el numero a cifrar: ")
m1 = []
m2 = []#Desencriptacion
c = []#Encriptacion
p = 0
q = 0
#Limites para hallar los dos numeros primos p y q
min = 1000
max = 10000
#Variable usada para determinar si un numero aleatorio es primo o no
esPrimo = True

#Se usa un ciclo para encontrar el primer numero p
while esPrimo:
    p = random.randint(min, max)
    if Primos.fermat(p):
        esPrimo = False

esPrimo = True

#Se usa un ciclo igual para encontrar el segundo numero q
while esPrimo:
    q = random.randint(min, max)
    if Primos.fermat(q):
        esPrimo = False

print("Primo p:", str(p))
print("Primo q:", str(q))

n = str(p*q)
# Se toma la cadena recibida y se convierte un subcadenas de tamaño menor a n
u = ""
for i in range(0, len(m)):
    if len(u) == len(n)-1:
        m1.append(int(u))
        u = m[i]
    else:
        u += m[i]
    if i == len(m)-1:
        m1.append(int(u))

publicKey = []
privateKey = []

# Se llama a los metodos que generan el par de llaves
publicKey, privateKey = GenerateKeys.keyGenerator(p, q)

print("Encriptación: ")

# Con las llave publica se llama a power mod, que calcula el cifrado de cada subcadena
for i in range(0, len(m1)):
    z = GenerateKeys.powerMod(m1[i], publicKey[0], publicKey[1])
    # Se concatena a c, para luego desencriptar
    c.append(z)
print(c)

print("Desencriptación: ")

#Con la llave privada se llama a power mod, que calcula el descifrado de cada subcadena
for i in range(0, len(m1)):
    z = GenerateKeys.powerMod(c[i], privateKey[0], publicKey[1])
    m2.append(z)
print(m2)
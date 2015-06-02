__author__ = 'estma_000'

import GenerateKeys

m = "71658479"
m1 = []
c = []
n = str(47*71)

u = ""
for i in range(0, len(m)):
    if len(u) == len(n)-1:
        m1.append(int(u))
        u = m[i]
    else:
        u += m[i]
    if i == len(m)-1:
        m1.append(int(u))

print(m1)

publicKey = []
privateKey = []

publicKey, privateKey = GenerateKeys.keyGenerator(47, 71)

print("LLave: " + str(publicKey[0]))
print("Encriptación: ")

for i in range(0, len(m1)):
    z = GenerateKeys.powerMod(m1[i], publicKey[0], publicKey[1])
    print(z)
    c.append(z)

print("Desencriptación: ")

for i in range(0, len(m1)):
    z = GenerateKeys.powerMod(c[i], privateKey[0], publicKey[1])
    print(z)
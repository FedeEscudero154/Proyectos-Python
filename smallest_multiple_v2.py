import itertools
from funciones_utiles import isPrime

def mcm(n):
    primos = []
    primosDeN = {}
    for i in range (2, n+1):
        if isPrime(i):
            primos.append(i)

    for i in primos:
        while n % i == 0:
            n = n / i
            if not i in primosDeN:
                primosDeN[i] = 1
            else:
                primosDeN[i] = primosDeN[i] + 1
    return primosDeN

listaPrincipal = []
contador = 2
primos = set([])
while contador < 20:
    diccionarioSecundario = mcm(contador)
    listaPrincipal.append(diccionarioSecundario)
    primos.update(diccionarioSecundario.keys())

    contador += 1

numeros = 1
for primo in primos:
    maxExponente = 0
    for diccionarioSecundario in listaPrincipal:
        if primo in diccionarioSecundario:
            maxExponente = max(maxExponente,diccionarioSecundario[primo])

    print(primo,maxExponente)
    numeros = numeros*(primo**maxExponente)

print(numeros)
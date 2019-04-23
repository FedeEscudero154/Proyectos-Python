import itertools
from funciones_utiles import isPrime,contarRepetidos

def mcm(n):
    primos = []
    primosDeN = []
    for i in range (2, n+1):
        if isPrime(i):
            primos.append(i)

    for i in primos:
        while n % i == 0:
            n = n / i
            primosDeN.append(i)
    return primosDeN


listaPrincipal = []
contador = 2
primos = set([])
while contador < 20:
    listaSecundaria = mcm(contador)
    listaPrincipal.append(listaSecundaria)
    primos.update(listaSecundaria)

    contador += 1

numeros = 1
for primo in primos:
    maxExponente = 0    
    for listaSecundaria in listaPrincipal:
        maxExponente = max(maxExponente,contarRepetidos(listaSecundaria,primo))

    print(primo,maxExponente)   
    numeros = numeros*(primo**maxExponente)

print(numeros)
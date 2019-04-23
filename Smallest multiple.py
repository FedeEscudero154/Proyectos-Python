from math import sqrt
import itertools
def isPrime(numero):
	for i in range(2,int(sqrt(numero)) + 1):
		if numero % i == 0:
			return False
	return True


def mcm(n):
    primos = []
    primosDeX = []
    for i in range (2, n + 2):
        if isPrime(i):
            primos.append(i)

    for i in primos:
        while n % i == 0:
            n = n / i
            primosDeX.append(i)
    return primosDeX


listaPrincipal = []
contador = 1
while contador < 20:
    contador += 1
    listaSecundaria = mcm(contador)
    listaPrincipal += listaSecundaria

numeros = 0
for i in listaPrincipal:
    for z in range(21):
        if i == z:
            numeros += 1
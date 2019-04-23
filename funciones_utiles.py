from math import sqrt

def contarRepetidos(lista,n):
	res = 0
	for valor in lista:
		if valor == n:
			res+=1
	return res

def isPrime(numero):
	for i in range(2,int(sqrt(numero)) + 1):
		if numero % i == 0:
			return False
	return True


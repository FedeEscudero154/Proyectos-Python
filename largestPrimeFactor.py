from math import sqrt

def isPrime(numero):
	for i in range(2,int(sqrt(numero))+1):
		if numero % i == 0:
			return False
	return True

def largestPrimeFactor(n):
	numerosMenoresAn = range(2,int(sqrt(n))+1)
	numerosMenoresAn = numerosMenoresAn[::-1]
	
	for proximoNumero in numerosMenoresAn:
		if isPrime(proximoNumero) and n % proximoNumero == 0:
			return proximoNumero

largestPrime = largestPrimeFactor(600851475143)
print(largestPrime)

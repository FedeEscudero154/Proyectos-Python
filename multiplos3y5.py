
def multiplosDe(n):
	mutiplos = []
	ultimoNumero = n

	while ultimoNumero < 1000:
		mutiplos.append(ultimoNumero)
		ultimoNumero = ultimoNumero + n

	return mutiplos

multiplos3 = multiplosDe(3)
multiplos5 = multiplosDe(5)

conjuntoFinal = set(multiplos5+multiplos3)
print(sum(conjuntoFinal))
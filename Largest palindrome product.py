def palindrome(n):
    resultado = []
    while n > 99:
        for i in range(1000, 100,-1):
            multiplicacion = i * n
            if str(multiplicacion) == str(multiplicacion)[::-1]:
                resultado.append(multiplicacion)           
        n = n - 1
    return max(resultado)

def test999():
	numero = palindrome(999)
	assert numero == 906609
	print(numero)

test999()
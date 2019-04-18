def palindrome(n):
    resultado = []
    while n > 899:
        for i in range(900, 1000):
            multiplicacion = i * n
            if str(multiplicacion) [0] == str(multiplicacion) [5] and str(multiplicacion) [1] == str(multiplicacion) [4] and str(multiplicacion) [2] == str(multiplicacion) [3]:
                resultado.append(multiplicacion)
            elif i == 999:
                n = n - 1
    return max(resultado)




n = 999
numero = palindrome(n)
print(numero)
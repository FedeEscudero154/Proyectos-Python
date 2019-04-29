from funciones_utiles import isPrime
#Primos = []
#for i in range(2,1000000000):
#    if isPrime(i):
#        Primos.append(i)
#        if len(Primos) == 10001:
#           break
#print(Primos[10000])

def Criba(n):
    Primos = []
    NoPrimos = []
    whileloop = n * 5
    for i in range(2, 10000000000):
        if isPrime(i):
            if n == 10000:
                break
            else:
                Primos.append(i)
                n = n - 1
                resultado = 0
                siguienteValor = i
                while resultado < whileloop:
                    siguienteValor = i
                    resultado = siguienteValor + i
                    NoPrimos.append(resultado)
                    siguienteValor = resultado
        else:
            continue
    return Primos
n = 10001
termina = Criba(n)
print(termina)
assert Primos[1] == 3 and n == 9999
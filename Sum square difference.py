squareOfTheSum = []
sumOfTheSquares = []
for i in range(1, 101):
    squareOfTheSum.append(i)
    cuadrado = i ** 2
    sumOfTheSquares.append(cuadrado)
resultado = (sum(squareOfTheSum)) ** 2 - sum(sumOfTheSquares)
print(resultado)

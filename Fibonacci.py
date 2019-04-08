
def fiboNVeces(n):
    num_anterior = 0
    num_siguiente = 1
    contador = 0
    serie = []
    if n == 1:
        serie.append(1)
    elif n == 2:
        serie.append(1)
        serie.append(2)
    else:
        while contador < n:
            serie.append(num_anterior)
            aux = num_siguiente
            num_siguiente = num_siguiente + num_anterior
            num_anterior = aux
            contador += 1

    return serie

def fiboMenorA(n):
    num_anterior = 0
    num_siguiente = 1
    serie = []
    if n == 1:
        serie.append(1)
    elif n == 2:
        serie.append(1)
        serie.append(2)
    else:
        while num_anterior < n:
            serie.append(num_anterior)
            aux = num_siguiente
            num_siguiente = num_siguiente + num_anterior
            num_anterior = aux

    return serie


def test_caso_de_10_numeros():
    valores = fibo(10)
    assert len(valores) == 10
    assert valores[0] == 0
    assert valores == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_caso_de_3_fibonacci():
    valores = fibo(10)
    assert valores[2] == 1


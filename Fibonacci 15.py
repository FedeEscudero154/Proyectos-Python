def fib(n):
	if n >= 1:
		num_anterior = 1
		print(num_anterior)
	if n >= 2:
		num_siguiente = 2
		print(num_siguiente)
	if n >= 3:
		for i in range(n-2):
		    if i != n-2:
		        resultado = num_siguiente + num_anterior
		        print(resultado)
		        num_anterior = num_siguiente
		        num_siguiente = resultado
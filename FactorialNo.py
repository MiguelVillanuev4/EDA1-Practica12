def factorial_no_recursivo(numero):
    fact=1
    for i in range(numero, 1, -1):
        fact = fact * i 
    return fact

factorial_no_recursivo(5)

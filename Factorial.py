def factorial_recursivo(numero):
    if numero<2:
        return 1
    return numero* factorial_recursivo(numero - 1)

factorial_recursivo(5)

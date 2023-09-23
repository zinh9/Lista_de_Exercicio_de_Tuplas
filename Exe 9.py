def pares(numeros):
    par = []
    
    for i in numeros:
        if i % 2 == 0:
            par.append(i)
    
    par = tuple(par)
    
    return par

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
par = pares(numeros)

print(par)

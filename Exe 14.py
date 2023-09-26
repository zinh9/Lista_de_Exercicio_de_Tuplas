def verifica(numeros):
    numeros = list(numeros)
    not_repetidos = []
    i = 1
    j = 1

    for n in numeros:
        while j < len(numeros):
            if n == numeros[j]:
                not_repetidos.append(i)
                numeros.remove(i)
            
            j += 1
        
        i += 1
        j = i
    
    numeros = tuple(numeros)
    not_repetidos = tuple(not_repetidos)

    print(f"Numeros: {numeros}")
    print(f"Numeros repetidos removidos: {not_repetidos}")

numeros = (1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 9, 10, 10)
verifica(numeros)

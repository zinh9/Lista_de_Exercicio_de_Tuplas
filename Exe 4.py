def soma(numeros):
    lista_numeros = list(numeros)
    soma = lista_numeros[0]
    i = 1
    
    while i < len(lista_numeros):
        soma += lista_numeros[i]
        
        i += 1
    
    return soma

numeros = (44, 66, 89, 34, 67, 111, 346, 902)
soma_numeros = soma(numeros)

print(soma_numeros)

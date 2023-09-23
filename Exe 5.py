def maior(numeros):
    maior = numeros[0]  # Inicialize a variável 'maior' com o primeiro elemento da tupla
    
    for n in numeros:
        if n > maior:
            maior = n
    
    return maior

numeros = (1, 4, 7, 10, 11, 98, 100, 4, 55, 2)
maior_numero = maior(numeros)

print(maior_numero)

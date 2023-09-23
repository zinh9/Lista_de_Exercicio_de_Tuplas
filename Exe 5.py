def maior(numeros):
    maior = numeros[0]  # Inicialize a variável 'maior' com o primeiro elemento da tupla
    
    for n in numeros:
        if n > maior:
            maior = n
    
    return maior

def menor(numeros):
    menor = numeros[0]
    
    for n in numeros:
        if n < menor:
            menor = n
    
    return menor
    
numeros = (1, 4, 7, 10, 11, 98, 100, 4, 55, 2)
maior_numero = maior(numeros)
menor_numero = menor(numeros)

print("O maior numero é:", maior_numero)
print("O menor numero é:", menor_numero)


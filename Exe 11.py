def media(numeros):
    media = 0
    i = 0
    
    while i < len(numeros):
        media += numeros[i]
        
        i += 1
    
    media /= len(numeros)
    
    print(f"A media dos numeros é: {media}")

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
media(numeros)

def pares_true_not(numeros):
    true_pares = []
    not_pares = []

    for i in numeros:
        if i % 2 == 0:
            true_pares.append(i)
        
        else:
            not_pares.append(i)
    
    if len(true_pares) == len(numeros):
        print("Todos os numeros são pares")
    
    elif len(true_pares) < len(numeros):
        print(f"Nem todos os numeros são pares: {len(true_pares)} pares e {len(not_pares)} impares")
    
    elif len(true_pares) == 0:
        print("Não tem nenhum numero par")

numeros = (1, 4, 678, 23, 34, 3, 8, 0, 4, 1, 3, 6, 2354, 148679, 1000000)
pares_true_not(numeros)

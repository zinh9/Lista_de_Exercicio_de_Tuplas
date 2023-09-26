def soma_tuplas(tupla_1, tupla_2):
    soma_1 = 0
    soma_2 = 0
    i = 0

    for i in tupla_1:
        soma_1 += i
    
    for i in tupla_2:
        soma_2 += i
    
    soma_total = soma_1 + soma_2

    print(f"Soma das tuplas: {soma_total}")

tupla_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
tupla_2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
soma_tuplas(tupla_1, tupla_2)

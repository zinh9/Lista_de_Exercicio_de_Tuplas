def verificar(numeros, numero_usu):
    for i in numeros:
        if numero_usu == i:
            esta = True
            break
        
        else:
            esta = False
    
    if esta == True:
        print("O numero está presente!")
    
    else:
        print("O numero não está presente!")
    
numero_usu = int(input("Digite um numero: "))
numeros = (22, 13, 55, 3, 11, 47, 44, 26, 1)
verificar(numeros, numero_usu)

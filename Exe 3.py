def ordem(cores):
    lista_cores = list(cores)
    lista = []
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for letra in alfabeto:
        for cor in lista_cores:
            if cor[0] == letra:
                lista.append(cor)
    
    i = 0 
    j = 1 
    
    return lista

cores = ("azul", "amarelo", "verde", "vermelho", "roxo", "branco", "preto")
lista_cores = ordem(cores)
tupla_ordenada = tuple(lista_cores)

print(tupla_ordenada)

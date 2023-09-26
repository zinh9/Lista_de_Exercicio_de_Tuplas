def pais_populoso(pais_populacao):
    mais_populoso = 0
    i = 0
    j = 1

    while j < len(pais_populacao):
        aux_1 = pais_populacao[i]
        aux_2 = pais_populacao[j]

        if aux_1[1] > aux_2[1]:
            mais_populoso = aux_1
        
        i = j
        j += 1
    

    return mais_populoso

pais_populacao = [("brasil", 214300000), ("angola", 34500000), ("canada", 38250000), ("russia", 143300000)]
mais_populoso = pais_populoso(pais_populacao)

print(f"O pais mais populoso é: {mais_populoso}")

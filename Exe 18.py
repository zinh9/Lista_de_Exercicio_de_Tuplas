def ordem(aluno_notas):
    aluno_notas = [(nota[1], nota[0]) for nota in aluno_notas]
    
    aluno_notas.sort()
    
    aluno_notas = [(aluno[1], aluno[0]) for aluno in aluno_notas]
    
    return aluno_notas
    
aluno_notas = [("enzo", 10), ("mariana", 8), ("luck", 0), ("kaynan", 6)]
nova_tupla = ordem(aluno_notas)

for i in nova_tupla:
    print(f"{i[0]}: {i[1]} pontos")

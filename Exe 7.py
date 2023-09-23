strings = ("mariana", "enzo", "sos", "amongus", "IFES", "televisão")
lista = []

for i in strings:
    if len(i) > 5:
        lista.append(i)

nova_tupla = tuple(lista)

print(nova_tupla)

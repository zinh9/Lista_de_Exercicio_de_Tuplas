palavras = ("caneta", "azul", "azul", "caneta", "caneta", "que", "esta", "marcada", "com", "a", "minha", "letra")
comprimento = []

for p in palavras:
    comprimento.append(len(p))

comprimento = tuple(comprimento)

print(f"Palavras: {palavras}")
print(f"Comprimento de cada palavra: {comprimento}")

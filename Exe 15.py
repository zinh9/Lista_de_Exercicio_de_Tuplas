def encontrar_fruta(frutas, fruta_usu):
    encontrei = False

    for fruta in frutas:
        if fruta_usu == fruta:
            encontrei = True
    
    return encontrei

frutas = ("maçã", "uva", "laranja", "banana", "morango", "limão", "pera", "mamão")
fruta_usu = input("Digite uma fruta: ")
encontrei = encontrar_fruta(frutas, fruta_usu)

if encontrei == True:
    print("A fruta que você digitou está na tupla!")

else:
    print("A fruta que você digitou não está na tupla!")        

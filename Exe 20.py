def ordem_alfabetica(animais):
    animais = list(animais)
    animais.sort()
    animais = tuple(animais)
    
    for i in range(3):
        print(animais[i])

animais = ("leão", "onça", "camelo", "orca", "macaco", "girafa", "orangotango", "peixe", "veado", "anta")
ordem_alfabetica(animais)

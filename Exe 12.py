def ordem_datas(datas):
    datas = [(data[2], data[1], data[0]) for data in datas]
    
    datas.sort()
    
    datas = [(data[2], data[1], data[0]) for data in datas]
    
    for data in datas:
        print(data)

datas = [(23, 4, 2005), (15, 4, 2005)]
ordem_datas(datas)

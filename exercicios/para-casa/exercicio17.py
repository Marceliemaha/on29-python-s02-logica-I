def calculo_tinta(metragem): 
    litros = metragem / 6 #descobrindo quantos litros de tinta precisa.
    latas = litros // 18 #descobrindo a quantidade de inteira de latas
    galoes = (litros % 18) / 3.6 #resto da quantidade de latas / pelo numero de galoes
    preco = (latas * 80) + (galoes * 25)  #descobrindo o preço total
    print("são necessária", latas, "latas e ", galoes, "galoes")
    print("com custo de", preco, "reais" )

calculo_tinta(1000)
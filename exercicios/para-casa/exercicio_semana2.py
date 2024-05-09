
#PROGRAMA PARA LOJA DE TINTA
#DEVERÁ PEDIR O TAMANHO EM METROS QUADRADOS DA ÁREA A SER PINTADA
#COBERTURA DA TINTA É DE 1 LITRO PARA CADA 3 METROS QUADRADOS
#TINTA VENDIDDA EM LATAS DE 18 LITROS, PR R$80,00
#INFORMAR AO USUÁRIO A QNTD. DE LATAS DE TINTA A SEREM COMPRADAS 
#INFORMAR AO USUÁRIO O PREÇO TOTAL

#1L COBRE 3 METROS QUADRADOS
#18L/1 LATA, COBRE 54 METROS QUADRADOS




def calculo_tinta(metragem): 
    litros = metragem / 3 #descobrindo quantos litros de tinta precisa.
    latas = litros / 18 #descobrindo a quantidade de latas
    preco = latas * 80 #descobrindo o preço total
    print("são necessária", latas, "latas")
    print("com custo de", preco, "reais" )

calculo_tinta(1000)




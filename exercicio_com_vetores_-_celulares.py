'''
Uma determinada loja possui 3 tipos de celulares, com suas quantidades e preços correspondentes

1 - calcule o total do valor do estoque de todos os celulares usando o produto interno
2 - calcule o total do valor do estoque DOBRADO de todos os celulares usando o produto interno

Este código demonstra que em qualquer posição que você multiplica os valores, seja os estoques, os valores unitários ou o produto interno, o resultado será o mesmo
'''

quantidade = [32, 129, 137] #lista de estoque com a quantidade de celulares
precos = [1903.65, 729.75, 5069.4] #preço de cada celular

estoque = list(zip(quantidade, precos))

#1
valor_estoque_celular = [(a * b) for a, b in estoque] #valor total de cada celular conforme o estoque
valor_total_estoque = sum(valor_estoque_celular) #valor total do estoque de todos os celulares

print(f"""Valor total do estoque de cada celular: {valor_estoque_celular}
Valor total de todo o estoque: {valor_total_estoque}
""")

#2 dobrando o valor do estoque
valor_estoque2_celular_prova = [(2 * a * b) for a, b in estoque] #valor total de cada celular conforme o estoque DOBRADO
valor_total_estoque2_prova = sum(valor_estoque2_celular_prova) #valor total do estoque DOBRADO de todos os celulares

print(f"""Prova do valor total do estoque DOBRADO de cada celular: {valor_estoque2_celular_prova}
Prova do valor total de todo o estoque DOBRADO: {valor_total_estoque2_prova}
""")

#2 dobrando o valor do estoque total (ou produto interno do #2 anterior)
valor_total_estoque2 = valor_total_estoque * 2 #calculando o produto interno do estoque DOBRADO apenas duplicando o produto interno de 1 ao invés de duplicar o estoque de 1

print(f"""Valor total de todo o estoque DOBRADO duplicando o p.i. do estoque normal: {valor_total_estoque2}
""")

#2 dobrando o valor dos preços unitários
valor_estoque3_celular = [(a * (2 * b)) for a, b in estoque]
valor_total_estoque3 = sum(valor_estoque3_celular)

print(f"""Valor total do estoque de cada celular com o valor unitário DOBRADO: {valor_estoque3_celular}
Valor total de todo o estoque com o valor unitário DOBRADO: {valor_total_estoque3}
""")

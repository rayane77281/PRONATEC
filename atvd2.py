def calcula_litros_comprados(preço_litro, valor_desejado):
    litro_comprados = valor_desejado / preço_litro
    return litro_comprados
preco_litro = 6.19
valor_desejado = 50.90
litros =calcula_litros_comprados(preco_litro, valor_desejado)
print(f"com R${valor_desejado:}, serao comprados {litros:.2f}litros de conbustivel.")

 
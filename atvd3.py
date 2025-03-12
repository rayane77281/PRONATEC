def converter_real_para_real(valor_dolar):
    taxa_conversao = 5.79
    valor_real = valor_dolar * taxa_conversao
    return valor_real
valor_dolar = 867
valor_em_real = converter_real_para_real(valor_dolar)
print(f"${valor_em_real} equivale a R${valor_em_real:.2f}.")
def verifica_numero():
    numero = int(input("digite um numero inteiro: "))
    if numero > 0:
        print("o numero e positivo,")
    elif numero < 0:
        print("o numero e negativo.")
    else:
        print("o numero e nulo (zero).")

verifica_numero()
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 +nota3) /3
    if media >=6.0:
        situaçao = "aprovado"
    else:
        situaçao = "reprovado"

    return media, situaçao
nota1 = 7.5
nota2 = 6.0
nota3 = 5.5
media, situaçao = calcular_media(nota1, nota2, nota3)
print(f"media: {media:2f} - situaçao: {situaçao}")
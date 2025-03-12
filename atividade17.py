senha_correta = "123"
usuario = "aluno"
while True:
    usuario_input = input("digite o usuario: ")
    senha_input = input("digite a senha: ")
    if usuario_input == "aluno" and senha_input == senha_correta:
        print("acesso permitido!")
        break
    else:
        print("usuario ou senha incorretos. tente novamente. /n")
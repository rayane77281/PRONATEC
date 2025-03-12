while True:
    resposta = input("deseja continua?  (S/N): ").strip().upper()
    if resposta == "N":
        print("programa encerrado.")
        break
    elif resposta == "S":
        print("continuando.../n")
    else:
        print("opçao invalida! digite 'S' para sim ou 'N' para nao./n")
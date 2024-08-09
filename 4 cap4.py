# Exercício do livro Capítulo 4 questão 4

c = input("Digite seu nome: ")
ch = 3
for x in range(1, 4):
    s = input("Digite sua senha: ")
    ch -= 1
    if s == 123456:
        print("Olá, {}. Seja bem-vindo ao nosso banco!".format(c))
        break
    elif ch == 2 or ch == 1:
        print(f"Senha incorreta! Você ainda tem {ch} tentativas.")

    if ch == 0:
        print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas")

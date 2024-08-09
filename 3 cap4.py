#Exercício do Capítulo 4 questão 3

pm = float("inf")
menor_nome_remedio = " "
preco_total = 0
for x in range (1, 5):
    n = input("Digite o nome do remédio: ")
    p = float(input("Digite o preço desse remédio: "))
    preco_total += p

    if p < pm:
        pm = p
        menor_nome_remedio = n
print("O seu menor preço de remédio é {:.2f} e seu nome é {}".format(pm, menor_nome_remedio))

media = preco_total / 5
print("Sua média total de preço por cada remédio é {:.2f}".format(media))


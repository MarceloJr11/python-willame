##Exercício do Capítulo 4 questão 3

n = input("Digite o nome do remédio: ")
p = float(input("Digite o preço desse remédio: "))
sp = 0
maisb = n
menorp = p
sp += p
for x in range (1, 5):
    n = input("Digite o nome do remédio: ")
    p = float(input("Digite o preço desse remédio: "))
    sp += p
    
    if p < menorp:
        menorp = p
        maisb = n
    
print("O nome do remédio mais barato é '{}' e seu preço é {:.2f}".format(maisb, menorp))

media = sp / 5
print("Sua média total de preço por cada remédio é {:.2f}".format(media))

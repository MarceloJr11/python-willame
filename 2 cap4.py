#Exercício do livro

p1 = int(input("Digite o primeiro termo da sua Progressão Aritmética (PA): "))
qt = int(input("Digite a quantidade de termo da sua Progressão Aritmética (PA): "))
r = int(input("Digite a razão da sua Progressão Aritmética (PA): "))

pa = 0
p = p1 + (qt - 1) * r
for x in range(p1, p + 1, r):
    pa += x
print("Sua Progressão aritmética(PA) é {}".format(pa))

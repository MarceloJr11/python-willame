#Exercício do livro

a = int(input("Digite um número inteiro: "))
b = int(input("Digite um outro número inteiro: "))

soma = 0
if a < b: 
    for x in range(a, b):
        soma += x
    print("A soma total dos números inteiros do seu intervalo, entre seu primeiro e segundo número é {}".format(soma))
else:
 print("Erro seu segundo número é maior que o primeiro")

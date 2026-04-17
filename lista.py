#Você é um professor de programação iniciante. Escreva um programa que imprima "Hello, World!".
print("Hello, World!")

#Em uma eleição escolar, crie um programa que leia a idade de um aluno e diga se ele pode votar: se >= 16 anos, "Pode votar!"; senão, "Ainda não pode votar.".
idade = int(input("Digite sua idade: "))
if idade >= 16:
    print("Pode votar!")
    else:
    print("Ainda não pode votar.")

#No supermercado, um cliente quer somar o valor de itens até digitar 0. Use while para ler
produto1 = float(input("quanto custa o produto?"))
produto2 = float(input("quanto custa o produto?"))

soma = produto1 + produto2

print(soma)

#Crie uma função que receba o peso e altura de uma pessoa (para academia) e categorize o IMC: magro (24.9). Use if-else e try-except para entradas inválidas.
peso = int(input("digite a peso: "))
altura = int(input("digite a altura: "))

imc = peso / (altura ** 2)

if imc <= 24 
        print("magro")
    else:
        print("gordo")

#Você tem uma lista de nomes de amigos em uma festa. Some a quantidade de amigos e verifique se é par ou ímpar com if-else.

#Registre 7 temperaturas diárias da semana em uma lista e calcule/imprima a média usando for.
fila = []

def validar_temperatura():
    while True:
        try:
            temperatura = int(input("Digite a temperatura: "))
            temperatura = int(input("Digite a tempetratura: "))
            temperatura = int(input("Digite a tempetratura: "))
            temperatura = int(input("Digite a tempetratura: "))
            temperatura = int(input("Digite a tempetratura: "))
            temperatura = int(input("Digite a tempetratura: "))
            temperatura = int(input("Digite a tempetratura: "))


def mostrar_fila():

    if len(validar_temperatura) == 0:
        print("Fila vazia!\n")
        return
    
    print("\n--- covidados ---")
    for i, temperatura in enumerate(validar_temperatura, start=1):
    print()


            
# Em uma lista de números de vendas de uma loja, use for para somar apenas os valores pares e imprimir o resultado.

#Em uma loja online, aplique desconto: >500 reais = 20%, 200-500=10%, <200=nenhum. Leia valor e imprima preço final.
valor = float(input("Valor: "))

if valor > 500:
    valor *= 0.8
elif valor >= 200:
    valor *= 0.9

print("Preço final:", valor)

#Em uma lista de notas de alunos, conte quantas estão acima de 7 e imprima o resultado usando for e if.
notas = [6, 8, 7.5, 5, 9, 4, 10]

contador = 0

for nota in notas:
    if nota > 7:
        contador += 1

print("Notas acima de 7:", contador)

#Conte vogais em uma frase digitada pelo usuário (ex: análise de texto para rede social).

#Ordene uma lista de 5 idades de alunos em ordem crescente.

#Crie um menu simples de calculadora com while: 1-soma, 2-subtração, 3-multiplicação, 4-divisão, 5-sair. Use if-else e try-except.
while True:
    print("\n1-Soma  2-Subtração  3-Multiplicação  4-Divisão  5-Sair")
    opcao = input("Escolha: ")

    if opcao == "5":
        print("Saindo...")
        break

    try:
        n1 = float(input("Número 1: "))
        n2 = float(input("Número 2: "))

        if opcao == "1":
            print("Resultado:", n1 + n2)
        elif opcao == "2":
            print("Resultado:", n1 - n2)
        elif opcao == "3":
            print("Resultado:", n1 * n2)
        elif opcao == "4":
            print("Resultado:", n1 / n2)
        else:
            print("Opção inválida!")

    except ValueError:
        print("Digite apenas números!")
    except ZeroDivisionError:
        print("Não pode dividir por zero!")
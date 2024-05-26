#1
letra = input("Digite uma letra: ")

if letra.lower() in 'aeiou':
    print("É uma vogal.")
else:
    print("É uma consoante.")





#2
preco_produto1 = float(input("Digite o preço do primeiro produto: "))
preco_produto2 = float(input("Digite o preço do segundo produto: "))
preco_produto3 = float(input("Digite o preço do terceiro produto: "))

menor_preco = min(preco_produto1, preco_produto2, preco_produto3)

if menor_preco == preco_produto1:
    print("Compre o primeiro produto.")
elif menor_preco == preco_produto2:
    print("Compre o segundo produto.")
else:
    print("Compre o terceiro produto.")






#3
numeros = []

for i in range(3):
    numeros.append(float(input(f"Digite o {i+1}º número: ")))

numeros.sort(reverse=True)
print("Números em ordem decrescente:", numeros)





#4
turno = input("Em qual turno você estuda? (M-matutino, V-vespertino, N-noturno): ")

if turno.upper() == 'M':
    print("Bom Dia!")
elif turno.upper() == 'V':
    print("Boa Tarde!")
elif turno.upper() == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido!")






#5
numero = int(input("Digite um número de 1 a 7: "))

dias_da_semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

if numero >= 1 and numero <= 7:
    print("O dia correspondente é", dias_da_semana[numero - 1])
else:
    print("Valor inválido. Digite um número entre 1 e 7.")






#6
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 9:
    conceito = 'A'
elif 7.5 <= media < 9:
    conceito = 'B'
elif 6 <= media < 7.5:
    conceito = 'C'
elif 4 <= media < 6:
    conceito = 'D'
else:
    conceito = 'E'

print("Notas:", nota1, "e", nota2)
print("Média:", media)
print("Conceito:", conceito)

if conceito in 'ABC':
    print("APROVADO")
else:
    print("REPROVADO")





#7
ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano", ano, "é bissexto.")
else:
    print("O ano", ano, "não é bissexto.")





#8
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação desejada (+, -, *, /, **): ")

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    resultado = num1 / num2
elif operacao == '**':
    resultado = num1 ** num2
else:
    print("Operação inválida.")
    resultado = None

if resultado is not None:
    print("Resultado:", resultado)

    if resultado % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")

    if resultado >= 0:
        print("O número é positivo.")
    else:
        print("O número é negativo.")

    if resultado.is_integer():
        print("O número é inteiro.")
    else:
        print("O número é decimal.")





#9
idade = int(input("Digite sua idade: "))

if 0 <= idade <= 150:
    print("Idade:", idade)
else:
    print("Valor inválido. A idade deve estar entre 0 e 150.")





#10
soma = 0
media = 0

for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    soma += numero

media = soma / 5

print("Soma dos números:", soma)
print("Média dos números:", media)





#11
numero = int(input("Digite um número inteiro: "))

if numero > 1:
    for i in range(2, numero):
        if (numero % i) == 0:
            print(numero, "não é um número primo.")
            break
    else:
        print(numero, "é um número primo.")
else:
    print(numero, "não é um número primo.")





#12
temperaturas = []

for i in range(5):
    temperatura = float(input(f"Digite a temperatura {i+1}: "))
    temperaturas.append(temperatura)

menor_temp = min(temperaturas)
maior_temp = max(temperaturas)
media_temp = sum(temperaturas) / len(temperaturas)

print("Menor temperatura:", menor_temp)
print("Maior temperatura:", maior_temp)
print("Média das temperaturas:", media_temp)






#13
saldo_medio = float(input("Digite o saldo médio do cliente: "))

if saldo_medio <= 200:
    credito = saldo_medio * 0.1
elif 200 < saldo_medio <= 300:
    credito = saldo_medio * 0.2
elif 300 < saldo_medio <= 400:
    credito = saldo_medio * 0.25
else:
    credito = saldo_medio * 0.3

print("Saldo médio:", saldo_medio)
print("Valor do crédito:", credito)





#14
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

ano_aposentadoria = 65 - idade + 2024

print(nome + ", você poderá se aposentar em", ano_aposentadoria)





#15
valor_hora = float(input("Digite o valor da hora de trabalho: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas
desconto_ir = 0

if salario_bruto <= 2112:
    desconto_ir = 0
elif 2112 < salario_bruto <= 2826.65:
    desconto_ir = salario_bruto * 0.075
elif 2826.65 < salario_bruto <= 3751.05:
    desconto_ir = salario_bruto * 0.15
elif 3751.05 < salario_bruto <= 4664.68:
    desconto_ir = salario_bruto * 0.225
else:
    desconto_ir = salario_bruto * 0.275

salario_liquido = salario_bruto - desconto_ir - (salario_bruto * 0.03)
fgts = salario_bruto * 0.11

print("Salário Bruto:", salario_bruto)
print("Desconto do Imposto de Renda:", desconto_ir)
print("Desconto do Sindicato:", salario_bruto * 0.03)
print("FGTS:", fgts)
print("Salário Líquido:", salario_liquido)

"""EXERCÍCIOS PYTHON- ESTRUTURA SEQUENCIAL"""

'''faça um Programa que mostre a mensagem "Alo mundo" na tela'''

print('Alô Mundo')

'''Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número]'''

numero = input('digite um número')
print(f'o numero digitado foi: {numero}')

'''faça um Programa que peça dois números e imprima a soma.'''

numero_1 = int(input('digite um número'))
numero_2 = int(input('digite outro número'))
soma = numero_1 + numero_2
print(f'o resultado é: {soma}')

'''Faça um Programa que peça as 4 notas bimestrais e mostre a média'''
nota_1 = float(input('digite  a nota'))
nota_2 = float(input('digite  a nota'))
nota_3 = float(input('digite  a nota'))
nota_4 = float(input('digite  a nota'))
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
print(f'a média da sala é:{media}')

'''Faça um Programa que converta metros para centímetros'''

medida = float(input('digite a metragem:'))
media = medida * 100.00
print(f'o resultado em metros corresponde a:{media} centímetros')

'''Faça um Programa que peça o raio de um círculo, calcule e mostre sua área'''

entrada = float(input('digite o raio de um círculo'))
raio = 3.14159265359 * entrada ** 2
print(f'A área do círculo desejado é:{raio}')

'''Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário'''

base = 4
altura = 5
area = base * altura
print(f'em um quadrado de base 4 e altura 5, sua área é:{area}')
print(f'o dobro da área desse quadrado é: {area * 2}')

''' Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o 
total do seu salário no referido mês '''

salario = float(input('quanto você ganha por hora?'))
horas = float(input('quantas horas você trabalha por semana'))
calculo = horas * salario * 4
print(f'Esse mês vocẽ receberá R$: {calculo} reais ')

'''Faça um Programa que peça a temperatura em graus Fahrenheit,transforme e mostre a temperatura em graus Celsius. 
C = 5 * ((F-32) / 9)'''

temperatura = float(input('digite o gram em Fahrenheit'))
temp = 5 * ((temperatura - 32) / 9)
print(f'O grau em Célcius equivale a: {temp} graus')

'''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit'''

temperatura = float(input('digite o gram em Célcius '))
temp = temperatura * 1.8 + 32
print(f'O grau em Fahrenheit equivale a: {temp} graus')

'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre'''

''' o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo '''

numero_1 = int(input('digite um número inteiro'))
numero_2 = int(input('digite outro número inteiro'))
numero_3 = float(input('agora digite um número real'))
print(numero_1 * 2 + numero_2 / 2)
print(numero_1 * 3 + numero_3)
print(numero_3 ** 2)

'''Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a 
seguinte fórmula: (72.7*altura) - 58'''

altura = float(input('digite sua altura'))
print(f'o seu peso ideal é: {72.7 * altura - 58}')

'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando 
as seguintes fórmulas:Para homens: (72.7*h) - 58 Para mulheres: (62.1*h) - 44.7'''

altura = float(input('digite sua altura'))
sexo = int(input(f'digite o sexo: [1] para masculino,[2] para feminino'))
f = 2
m = 1
if sexo <= 1:
    print(f'seu peso ideal é:{72.7 * altura - 58}')
if sexo >= 2:
    print(f'seu peso ideal é:{(62.1 * altura) - 47} ')

'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo 
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a 
variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite
 e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas'''

peso = float(input('digite a quantidade de peixe pescado'))

if peso <= 50:
    print('Parabéns, hoje você não paga nada de imposto')
if peso > 50:
    print(f' A pescaria foi boa, você pescou: {peso} kg de peixes')
    excedente = peso - 50
    print(f' Será cobrado o valor de R$:{excedente * 4.00} reais de peso excedente')

'''faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

    Obs.: Salário Bruto - Descontos = Salário Líquido'''

salario = float(input('quanto você ganha por hora?'))
horas = float(input('quantas horas você trabalha por semana?'))
calculo = horas * salario * 4
IR = calculo / 100 *11
INSS = calculo /100 * 8
Sindicato = calculo /100 * 5
Salario_liquido = calculo - IR - INSS - Sindicato
print(f'Salário bruto relativo ao mês é de: R$ {calculo}')
print(f'desconto IR = R$ {IR}')
print(f'desconto INSS = R$ {INSS}')
print(f'desconto Sindicato = R$ {Sindicato}')
print(f'total de descontos é de: R${ IR + INSS + Sindicato}')
print(f'Salário líquido é de: R$ {Salario_liquido}')


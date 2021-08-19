"""LISTA PYTHON BRASIL'''
https://wiki.python.org.br/EstruturaDeDecisao"""

'''1. Faça um Programa que peça dois números e imprima o maior deles.'''

num_1 = input('digite um número')
num_2 = input('digite outro número')
if num_1 >= num_2:
    print(num_1)
if num_2 >= num_1:
    print(num_2)

'''Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.'''

num = int(input('digite um número'))
if num > 0:
    print('esse número é positivo')
elif num < 0:
    print('esse número é negativo')
else:
    print('ah, seu número é zero :s')

'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
   F - Feminino, M - Masculino, Sexo Inválido.'''

letra = input('digite a primeira letra do seu sexo')
if letra == 'M':
    print('MASCULINO')
elif letra == 'F':
    print('FEMINO')
else:
    print('Seja o que quiser ser...')

'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''

letra = input('digite uma letra')

if letra in 'a,e,i,o,u':
    print('vogal')
else:
    print('não é vogal')

'''Faça um programa para a leitura de duas notas parciais de um aluno. 

O programa deve calcular a média alcançada por aluno e apresentar:

A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.'''

nota_1 = float(input('digite sua nota'))
nota_2 = float(input('digite sua próxima nota'))
media = nota_1 + nota_2 / 2

if media >= 7.0:
    print('Parabéns,você foi aprovado')
if media <= 7.0:
    print('Que pena! :( 5 Não foi dessa vez')
if media >= 10:
    print('Aprovado com Distinção')

'''Faça um Programa que leia três números e mostre o maior deles.'''
num_1 = input('digite um número')
num_2 = input('digite um número')
num_3 = input('digite um número')

if num_1 > num_2 and num_1 > num_3:
    print(f'o maior número é {num_1}')
if num_2 > num_1 and num_2 > num_3:
    print(f' maior número é {num_2}')
if num_3 > num_1 and num_3 > num_2:
    print(f'o maior número é {num_3}')

'''Faça um Programa que leia três números e mostre o maior e o menor deles.'''

num_1 = input('digite um número')
num_2 = input('digite um número')
num_3 = input('digite um número')

if num_1 > num_2 > num_3:
    print(f'o MAIOR número é : {num_1}')
if num_2 > num_1 > num_3:
    print(f'o MAIOR número é : {num_2}')
if num_3 > num_2 > num_1:
    print(f'o MAIOR número é : {num_3}')
if num_1 < num_2 < num_3:
    print(f'o MENOR número é : {num_1}')
if num_2 < num_1 < num_3:
    print(f'o MENOR número é : {num_2}')
if num_3 < num_2 < num_1:
    print(f'o MENOR número é ; {num_3}')

'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.'''

p1 = float(input('produto 1'))
p2 = float(input('produto 2'))
p3 = float(input('produto 3'))

if p1 < p2 < p3:
    print(f'o MENOR preço é o  produto 1  no valor de R$ :{p1}')
if p2 < p1 < p3:
    print(f'o MENOR preço é o  produto 2  no valor de R$ :{p2}')
if p3 < p2 < p1:
    print(f'o  MENOR preço é o  produto 3  no valor de R$ : {p3}')
elif p1 == p1 and p2 < p3:
    print(f'O produto 1 no valor de R$ {p1} e 2 no valor de R$ {p2} são os mais baratos!!')
elif p1 == p2 and p3 < p2:
    print(f'O produto 2 no valor de R$ {p2} e 3 no valor de R$ {p3} são os mais baratos!!')
elif p1 == p3 and p2 < p1:
    print(f'O produto 3 no valor de R$ {p3} e 2 n6 va36r de R$ {p2} são os mais baratos!!')

else:
    print('compra qualquer um! É tudo o mesmo preço')

'''Faça um Programa que leia três números e mostre-os em ordem decrescente.'''

n1 = input('digite um número')
n2 = input('digite outro número')
n3 = input('digite mais um número')

"""Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
 Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso."""

print('Para o turno norturno, digite N, para o turno da tarde, V e para o turno da manhã digite M')

t1 = input('digite seu turno de estudos')

if t1 == 'M':
    print('Olá, BOM DIA!')

elif t1 == 'V':
    print('Olá, BOA TARDE!')

elif t1 == 'N':
    print('Olá, BOA NOITE!')

else:
    print('valor inválido')

'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para
 desenvolver o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
baseado no salário atual:

salários até R$ 280,00 (incluindo) : aumento de 20%

salários entre R$ 280,00 e R$ 700,00 : aumento de 15%

salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%

o percentual de aumento aplicado;

o valor do aumento;

o novo salário, após o aumento.'''

salario = float(input('O meu salário é R$ '))
desc_1 = salario / 100 * 20 + salario
desc_2 = salario / 100 * 15 + salario
desc_3 = salario / 100 * 10 + salario

if salario <= 280.00:
    print(f'o salário atualizado é de: R$ {desc_1}')

elif salario >= 280.00 <= 700.00:
    print(f'o salário atualizado é de: R$ {desc_2}')

elif salario >= 700.00 <= 1500.00:
    print(f'o salário atualizado é de: R$ {desc_3}')

'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do 
Salário Bruto, mas não é descontado (é a empresa que deposita).

O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:

Salário Bruto até 900 (inclusive) - isento

Salário Bruto até 1500 (inclusive) - desconto de 5%

Salário Bruto até 2500 (inclusive) - desconto de 10%

Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
 No exemplo o valor da hora é 5 e a quantidade de hora é 220.

    Salário Bruto: (5 * 220)        : R$ 1100,00
    (-) IR (5%)                     : R$   55,00  
    (-) INSS ( 10%)                 : R$  110,00
    FGTS (11%)                      : R$  121,00
    Total de descontos              : R$  165,00
    Salário Liquido                 : R$  935,00'''

qtd_hr = float(input('Quantas horas por mês você trabalha? '))
hr = float(input('Qual o valor da sua hora? '))

sl = qtd_hr * hr
sind = sl * 3 / 100
ir = sl * 5 / 100
inss = sl * 10 / 100
fgts = sl * 11 / 100
desc = inss + ir
sl_liq = sl - desc

if sl <= 900.00:
    sl = sl - sind
    sl = sl - fgts

    print(f'salário bruto: R$ {sl:,.2f}')
    print(f'desconto IR: R$ {sl - ir - sl:,.2f}')
    print(f'desconto INSS: R$ {sl - inss - sl:,.2f} ')
    print(f'desconto FGTS: R$  {sl - fgts - sl:,.2f} ')
    print(f'desconto FGTS: R$  {sl - fgts - sl:,.2f} ')

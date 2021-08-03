LISTA PYTHON BRASIL-https://wiki.python.org.br/EstruturaDeDecisao

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
  print ('ah, seu número é zero :s')

'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
   F - Feminino, M - Masculino, Sexo Inválido.'''

letra = input('digite a primeira letra do seu sexo')
if letra =='M':
  print('MASCULINO')
elif letra == 'F':
  print('FEMINO')
else:
  print('Seja o que quiser ser...')

'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''

letra= input('digite uma letra')
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
media = nota_1 + nota_2 /2

if media >= 7.0:
  print('Parabéns,você foi aprovado')
if media <= 7.0:
    print('Que pena! :( 5 Não foi dessa vez')
if media >= 10:
  print('Aprovado com Distinção')

'''Faça um Programa que leia três números e mostre o maior deles.'''
num_1= input('digite um número')
num_2= input('digite um número')
num_3= input('digite um número')
if num_1 > num_2 and num_1 > num_3:
  print(f'o maior número é {num_1}')
if num_2 > num_1 and num_2 > num_3:
  print(f' maior número é {num_2}')
if num_3 > num_1 and num_3 > num_2:
  print(f'o maior número é {num_3}')

'''Faça um Programa que leia três números e mostre o maior e o menor deles.'''

num_1= input('digite um número')
num_2= input('digite um número')
num_3= input('digite um número')
if num_1 > num_2 and num_2 > num_3:
  print(f'o MAIOR número é : {num_1}')
if num_2 > num_1 and num_1 > num_3:
  print(f'o MAIOR número é : {num_2}')
if num_3 > num_2 and num_2 > num_1:
  print(f'o MAIOR número é : {num_3}')
if num_1 < num_2 and num_2 < num_3:
  print(f'o MENOR número é : {num_1}')
if num_2 < num_1 and num_1 < num_3:
  print(f'o MENOR número é : {num_2}')
if num_3 < num_2 and num_2 < num_1:
  print(f'o MENOR número é ; {num_3}')

'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.'''

p1 = float(input('produto 1'))
p2 = float(input('produto 2'))
p3 = float(input('produto 3'))

if p1 < p2 and p2 < p3:
  print(f'o MENOR preço é o  produto 1  no valor de R$ :{p1}')
if p2 < p1 and p1 < p3:
  print(f'o MENOR preço é o  produto 2  no valor de R$ :{p2}')
if p3 < p2 and p2 < p1:
  print(f'o  MENOR preço é o  produto 3  no valor de R$ : {p3}')
elif p1 == p1 and p2 < p3:
  print (f'O produto 1 no valor de R$ {p1} e 2 no valor de R$ {p2} são os mais baratos!!')
elif p1 == p2 and p3 < p2:
  print (f'O produto 2 no valor de R$ {p2} e 3 no valor de R$ {p3} são os mais baratos!!')
elif p1 == p3 and p2 < p1:
  print (f'O produto 3 no valor de R$ {p3} e 2 n6 va36r de R$ {p2} são os mais baratos!!')
else:
  print('compra qualquer um! É tudo o mesmo preço')


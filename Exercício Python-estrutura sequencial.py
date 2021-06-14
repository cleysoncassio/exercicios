''' EXERCÍCIOS PYTHON- ESTRUTURA SEQUENCIAL '''

#Faça um Programa que mostre a mensagem "Alo mundo" na tela.

print('Alô Mundo') #o comando( print), é utilizado para chamar a impressão da sentença escrita em forma de string.

#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

numero = input('digite um número')
print(f'o numero digitado foi: {numero}')

#Faça um Programa que peça dois números e imprima a soma.
numero_1 = int(input('digite um número')) # entrada de número a ser digitado. Atenção, se não colocar o int antes do input, o resultado será uma junção de dois numeros e não uma soma
numero_2 = int(input('digite outro número'))
soma= numero_1 + numero_2
print(f'o resultado é: {soma}')

#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota_1 = float(input('digite  a nota'))
nota_2 = float(input('digite  a nota'))
nota_3 = float(input('digite  a nota'))
nota_4 = float(input('digite  a nota'))
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
print(f'a média da sala é:{media}')

#Faça um Programa que converta metros para centímetros.

medida = float(input('digite a metragem:'))
media = medida * 100.00
print(f'o resultado em metros corresponde a:{media} centímetros')

'''Faça um Programa que peça o raio de um círculo, calcule e mostre sua área'''

entrada = float(input('digite o raio de um círculo'))
raio =  3.14159265359 * entrada ** 2
print(f'A área do círculo desejado é:{raio}')

"""Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário. """
base = 4
altura = 5
area = base * altura
print(f'em um quadrado de base 4 e altura 5, sua área é:{area}')
print(f'o dobro da área desse quadrado é: {area * 2}')


"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. """

salario = float(input('quanto você ganha por hora?'))
horas = float( input('quantas horas você trabalha por semana'))
calculo = horas * salario * 4
print(f'Esse mês vocẽ receberá R$: {calculo} reais ')


"""Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

    C = 5 * ((F-32) / 9). """

temperatura = float(input('digite o gram em Fahrenheit'))
temp = 5* ((temperatura -32) /9)
print(f'O grau em Célcius equivale a: {temp} graus')

"""Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. """
#para converter graus Celcius em Fahrenheit * por 1.8 e adicione 32

temperatura = float(input('digite o gram em Célcius '))
temp = temperatura * 1.8 + 32
print(f'O grau em Fahrenheit equivale a: {temp} graus')

"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo."""

numero_1 = int(input('digite um número inteiro'))
numero_2 = int(input('digite outro número inteiro'))
numero_3 = float(input('agora digite um número real'))
print(numero_1*2 +numero_2/2)
print(numero_1 * 3 +numero_3)
print(numero_3 **2)

"""Ten{do como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58"""

altura = float(input('digite sua altura'))
print(f'o seu peso ideal é: {72.7 * altura - 58}')

""" 13- Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7 """

altura = float(input('digite sua altura'))
sexo = int(input(f'digite o sexo: [1] para masculino,[2] para feminino'))
f = 2
m = 1
if sexo <= 1:
    print(72.7 * altura - 58)
if sexo <= 2:
    print((62.1*altura) - 44.7 )






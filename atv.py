#criacao da atv.py

#escreva um programa que le 3 numeros reais a,b e c,
#representando os coeficientes de uma equação do segundo grau. 
#seu programa deve calcular as raizes da equação e exibir conforme os exemplos de saida



import math

a = float(input("digite o valor de a: "))
b = float(input("digite o valor de b: "))
c = float(input("digite o valor de c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("a equação não possui raízes reais")
elif delta == 0:
    x = -b / (2*a)
    print("a equação possui uma raiz real:", x)
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("as raízes da equação são", x1, "e", x2)
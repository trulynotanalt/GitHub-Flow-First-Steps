
#Você tem um grupo de n
# estudantes que precisam de acesso a um curso online. Existem dois tipos de chaves de acesso disponíveis na loja:

#Chave individual: custa a
# dólares e dá acesso a um estudante.

#Chave em grupo: custa b
# dólares e dá acesso a um grupo de até três estudantes, inclusive.

#Uma chave em grupo também pode ser usada para menos estudantes (um ou dois), e seu preço não muda.

#Sua tarefa é determinar a quantidade mínima de dinheiro necessária para fornecer acesso ao curso online para todos os n
# estudantes.

#Entrada
#A primeira linha contém um inteiro t
# (1≤t≤10⁴)
# — o número de casos de teste.

#Cada caso de teste consiste em uma linha contendo três inteiros n, a, b
# (1≤n,a,b≤10⁸)
# — o número de estudantes, o custo de uma chave individual e o custo de uma chave em grupo.

#Saída
#Para cada caso de teste, imprima um inteiro — a quantidade mínima de dinheiro necessária para fornecer acesso ao curso online para todos os n
# estudantes.
```
t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())

    custo_grupo = min(b, 3 * a)

    resposta = (n // 3) * custo_grupo + (n % 3) * a

    print(resposta)
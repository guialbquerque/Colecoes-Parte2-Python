"""
Curso Collections parte 2 - Alura
"""
from collections import defaultdict
from collections import Counter

alunos_datascience = [15, 23, 56, 30]
alunos_machinelearning = [23, 56, 40, 18]

turma_completa = alunos_datascience.copy()
""""
O copy realiza uma copia rasa, pois considerando um objeto composto por outros objetos, classes, realiza apenas uma 
copia de referencia simples, diferentemente de um deepcopy, que copia todas as instancias e referencias.
"""
alunos_datascience.extend([1, 2, 3])
print(f'Aluno datascience: {alunos_datascience}')
print(turma_completa)
turma_completa.extend(alunos_machinelearning)
print(set(turma_completa))
""""
Quando é importante não haver elemento repetido, sempre usar set
"""
for i in set(turma_completa):
    print(i)

conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 2, 10, 11, 12, 15}
# print(conjunto[2])
""""
Nao eh possivel acessar posicoes de elementos num conjunto pois nao existe ordem dentro de um conjunto
"""

"""
Operacao Uniao com conjuntos
"""
print(f'Operacao Uniao com conjuntos - {set(alunos_datascience) | set(alunos_machinelearning)}')

"""
Operacao Interseccao - elementos que existem nos dois conjuntos 
"""
print(f'Operacao Interseccao - {set(alunos_datascience) & set(alunos_machinelearning)}')

"""
Elementos que só existem no primeiro conjunto excluindo elementos em comum com outro conjunto
"""
print(f'Elementos que só existem no primeiro conjunto, '
      f'excluindo os em comum com outro conjuntio: \n {set(alunos_datascience) - set(alunos_machinelearning)}')

"""
Operacao OU exclusivo, elementos que so existem ou em conjunto ou em outro
"""

print(f'Operacao OU exclusivo - {set(alunos_datascience) ^ set(alunos_machinelearning)}')

conjunto2.add(5)  # Metodo para adicionar elementos num conjunto
print(conjunto2)
conjunto2.add(13)
print(conjunto2)

conjunto2 = frozenset(conjunto2)
print(type(conjunto2))
# conjunto2.add(20) Nao é mais possivel adicionar elementos ja que este conjunto foi congelado
texto = "Meu nome eh joao o nome do Meu cachorro tambem eh joao"
print(set(texto.split()))
texto_dividido = texto.split()

print(texto_dividido)
print()
print("Numero de vezes que cada palavra aparece no texto")
dicionario = {}
for i in texto_dividido:
    dicionario[i] = texto_dividido.count(i)

print(dicionario)

"""
Maneiras de iterar um dicionario
"""
print("Quando somente as chaves do dicionario importa")
for chave in dicionario.keys():
    print(chave)

print("Quando somente os valores importa")
for valor in dicionario.values():
    print(valor)

print("Quando o par chave - valor importa")
for item in dicionario.items():
    print(item)

for chave, valor in dicionario.items():
    print(f'Chave: {chave} - Valor: {valor}')

"""
Segunda maneira de contar as palavras numa string e adicionar num dicionario padrao
"""

dicionario2 = defaultdict(int)
texto = texto.lower()
for p in texto.split():
    cont = dicionario2[p]
    dicionario2[p] = cont + 1

print(f'Dicionario usando dictdefault: \n{dicionario2}')

"""
Terceira maneira de contar as palavras
"""

novo_dict = Counter(texto.split())
print(f'Usando Counter: {novo_dict}')

print(Counter(texto))

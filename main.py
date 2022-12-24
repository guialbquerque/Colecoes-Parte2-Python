"""
Curso Collections parte 2 - Alura
"""

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
print(set(alunos_datascience) | set(alunos_machinelearning))

"""
Operacao Interseccao - elementos que existem nos dois conjuntos
"""
print(set(alunos_datascience) & set(alunos_machinelearning))

"""
Elementos que só existem no primeiro conjunto excluindo elementos em comum com outro conjunto
"""
print(set(alunos_datascience) - set(alunos_machinelearning))

"""
Operacao OU exclusivo, elementos que so existem ou em conjunto ou em outro
"""

print(set(alunos_datascience) ^ set(alunos_machinelearning))

conjunto2.add(5)  # Metodo para adicionar elementos num conjunto
print(conjunto2)
conjunto2.add(13)
print(conjunto2)

conjunto2 = frozenset(conjunto2)
print(type(conjunto2))
# conjunto2.add(20) Nao eh mais possivel adicionar elementos ja que este conjunto foi congelado
texto = "Meu nome eh joao o nome do Meu cachorro tambem eh joao"
print(set(texto.split()))
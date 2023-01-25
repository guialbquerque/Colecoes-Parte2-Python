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
Quando é importante não haver elemento repetido, sempre usar set - criando assim um conjunto com elementos únicos
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
Operacao Interseccao - elementos que existem nos dois conjuntos ao mesmo tempo 
"""
print(f'Operacao Interseccao - {set(alunos_datascience) & set(alunos_machinelearning)}')

"""
Elementos que só existem no primeiro conjunto excluindo elementos em comum com outro conjunto
"""
print(f'Elementos que só existem no primeiro conjunto, '
      f'excluindo os em comum com outro conjunto: \n {set(alunos_datascience) - set(alunos_machinelearning)}')

"""
Operacao OU exclusivo, elementos que so existem ou em um conjunto ou em outro
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
print(set(texto.lower().split()))
texto_dividido = texto.lower().split()

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
O default_factory sendo int, retorna zero caso a chave que se busca no dicionario nao exista, evitando keyerror
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
"""
É interessante notar acima como o Counter funcionou de forma diferente no mesmo texto. Ao usar o método split(), uma 
lista de strings foi criada, contando as strings. Passando o texto todo como única string, ele contou cada letra e
espaço.
"""

"""
Contador de letras - recuperando dois textos
"""

texto1 = """Pandas é uma biblioteca para Ciência de Dados de código aberto (open source), construída sobre a 
linguagem Python, e que providencia uma abordagem rápida e flexível, com estruturas robustas para se trabalhar com 
dados relacionais (ou rotulados), e tudo isso de maneira simples e intuitiva.

Apesar do nome da biblioteca ser associado ao mamífero da família de ursos, tal qual o Python é associado com a 
espécie de cobra erroneamente, o nome da biblioteca Pandas é derivado do termo Panel Data, um conceito em inglês 
relacionado ao campo de estudo da econometria.

De maneira geral, o Pandas pode ser utilizado para várias atividades e processos, entre eles: limpeza e tratamento de 
dados, análise exploratória de dados (EDA), suporte em atividades de Machine Learning, consultas e queries em bancos 
de dados relacionais, visualização de dados, webscraping e muito mais. E além disso, também possui ótima integração 
com várias outras bibliotecas muito utilizadas em Ciência de Dados, tais como: Numpy, Scikit-Learn, Seaborn, Altair, 
Matplotlib, Plotly, Scipy e outros. 

Dentro do pacote Pandas, temos dois objetos primários importantes: as Series e os 
DataFrames. E para entender um pouco melhor sobre essas estruturas, vamos utilizar como exemplo um conjunto de dados 
chamado Iris, que traz algumas informações a respeito de características de espécies das flores de Íris."""

texto2 = """Talvez você tenha o costume de tirar selfies e divulgar pelo mundo digital. Isso é bom, porque dá a você 
uma certa intimidade com a câmera. Mas, para o LinkedIn, a história é um pouco diferente.

A ideia é que, para uma rede social de trabalho, sua foto demonstre profissionalismo. Para isso, evite retratos com 
elementos como perucas, óculos engraçados ou caretas. Busque um fundo mais neutro e mostre mais o rosto — não é 
necessária uma foto de corpo.

Não se esqueça de um detalhe muito importante: um belo sorriso, que seja sincero e cativante. Nada de sorrisos 
amarelos e forçados, certo?

Logo abaixo da foto, estará o seu título profissional. O que isso significa? Que ali, no topo do perfil, 
estará descrito o seu cargo atual ou, então, a posição que deseja ocupar.

Para isso, o importante é ser direto e usar palavras-chave relacionadas ao cargo. Essa informação será fundamental 
para que possíveis contratantes o identifiquem como a pessoa que estão procurando."""

print("------------------------------------------------------------------------------")
print("Contando os 10 caracteres mais comuns em textos aleatorios e gerando frequencia")


def freq_de_caracteres_mais_comuns(texto):
    aparicoes = dict((Counter(texto)))
    total_aparicoes = sum(aparicoes.values())
    for caractere, frequencia in Counter(texto).most_common(10):
        print(f'{caractere} --> {(frequencia / total_aparicoes) * 100:.2f}%')


freq_de_caracteres_mais_comuns(texto1)
print("------------------------------")
freq_de_caracteres_mais_comuns(texto2)

"""
É interessante notar como os textos na língua portuguesa possuem uma distribuicaod e frequencia que se repete com os 
caracteres mais comuns independente do que se trata o texto.
"""
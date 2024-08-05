
# Criando uma lista
minha_lista = [1, 2, 3, 'Python', [4, 5]]

# Acessando um elemento
print(minha_lista[3])

# Modificando um elemento
minha_lista[1] = 'alterado'
print(minha_lista)


# 
# ## Tuplas
# 
# As tuplas são semelhantes às listas, mas com uma diferença fundamental: são imutáveis. Uma vez criada uma tupla, seus elementos não podem ser alterados, adicionados ou removidos.
# 
# ### Características:
# - **Mutabilidade**: Tuplas são imutáveis, não podem ser modificadas após a criação.
# - **Ordenação**: As tuplas mantêm a ordem dos elementos conforme são adicionados.
# - **Indexação**: Como as listas, as tuplas permitem acesso aos elementos por índices.
# - **Uso**: Úteis para armazenar dados que não devem ser alterados.
# 
# ### Exemplo de uso:
# 


# Criando uma tupla
minha_tupla = (1, 2, 3, 'Python')

# Acessando um elemento
print(minha_tupla[2])

# Tentando modificar um elemento (vai gerar um erro)
try:
    minha_tupla[1] = 'alterado'
except TypeError as e:
    print(f"Erro: {e}")


# 
# ## Dicionários
# 
# Os dicionários são coleções de pares chave-valor. Eles são mutáveis e não mantêm uma ordem específica dos elementos.
# 
# ### Características:
# - **Mutabilidade**: Os dicionários são mutáveis, permitindo a alteração, adição e remoção de pares chave-valor.
# - **Ordenação**: Antes do Python 3.7, os dicionários não mantinham a ordem dos elementos. A partir do Python 3.7, mantêm a ordem de inserção.
# - **Chaves Únicas**: As chaves em um dicionário devem ser únicas e imutáveis.
# - **Acesso**: Permite acesso aos valores através das chaves.
# 
# ### Exemplo de uso:
# 


# Criando um dicionário
meu_dict = {'nome': 'Python', 'ano': 1991, 'versão': 3.10}

# Acessando um valor
print(meu_dict['nome'])

# Modificando um valor
meu_dict['versão'] = 3.9
print(meu_dict)


# 
# ## Conjuntos
# 
# Os conjuntos são coleções não ordenadas de itens únicos. São mutáveis, mas os itens dentro de um conjunto devem ser imutáveis.
# 
# ### Características:
# - **Mutabilidade**: O conjunto em si é mutável, mas os elementos dentro dele devem ser imutáveis.
# - **Ordenação**: Conjuntos não mantêm a ordem dos elementos.
# - **Elementos Únicos**: Não permite elementos duplicados.
# - **Operações**: Suporta operações matemáticas de teoria dos conjuntos, como união, interseção e diferença.
# 
# ### Exemplo de uso:
# 


# Criando um conjunto
meu_conjunto = {1, 2, 3, 4, 4}

# Mostrando os elementos do conjunto
print(meu_conjunto)

# Adicionando um elemento
meu_conjunto.add(5)
print(meu_conjunto)

# Tentando adicionar um elemento duplicado (não terá efeito)
meu_conjunto.add(2)
print(meu_conjunto)
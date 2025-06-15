import pandas as pd
import numpy as np
from math import sqrt

# 1 - Números ímpares de uma lista  
def filtrar_impares(lista):
    return [x for x in lista if x % 2 != 0]

# 2 - Números primos em uma lista
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def filtrar_primos(lista):
    return [x for x in lista if eh_primo(x)]

# 3 - Elementos inclusivos em duas listas 
def elementos_unicos(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)
    diferenca1 = set1 - set2
    diferenca2 = set2 - set1
    return list(diferenca1.union(diferenca2))

# 4 - Segundomaior valor em uma lista
def segundo_maior(lista):
    if len(lista) < 2:
        raise ValueError("A lista deve conter pelo menos 2 elementos")
    lista_unica = list(set(lista))
    lista_unica.sort()
    return lista_unica[-2]

# 5 - Ordenar tuplas pelo nome
def ordenar_pessoas(pessoas):
 return sorted(pessoas, key=lambda pessoa: pessoa[0].lower())

# 6 - Tratar outliers 
def tratar_outliers_std(df, coluna):
    media = df[coluna].mean()
    desvio = df[coluna].std()
    filtro = (df[coluna] >= media - 3*desvio) & (df[coluna] <= media + 3*desvio)
    return df[filtro]

def tratar_outliers_quartis(df, coluna):
    Q1 = df[coluna].quantile(0.25)
    Q3 = df[coluna].quantile(0.75)
    IQR = Q3 - Q1
    filtro = (df[coluna] >= Q1 - 1.5*IQR) & (df[coluna] <= Q3 + 1.5*IQR)
    return df[filtro]

# 7 - Concatenar DataFrames
def concatenar_dataframes(lista_dfs, empilhar_linhas=True):
    axis = 0 if empilhar_linhas else 1
    return pd.concat(lista_dfs, axis=axis)

# 8 - Leitura de CSV e exibição das primeiras linhas
def ler_csv_e_mostrar(caminho, n_linhas=5):
    df = pd.read_csv(caminho)
    print(f"Primeiras {n_linhas} linhas do DataFrame:")
    print(df.head(n_linhas))
    return df

# 9 - Selecionar coluna e filtrar linhas 
def filtrar_dataframe(df, coluna, condicao, valor):
    if condicao == '>':
        return df[df[coluna] > valor]
    elif condicao == '<':
        return df[df[coluna] < valor]
    elif condicao == '==':
        return df[df[coluna] == valor]
    elif condicao == '!=':
        return df[df[coluna] != valor]
    elif condicao == '>=':
        return df[df[coluna] >= valor]
    elif condicao == '<=':
        return df[df[coluna] <= valor]
    else:
        raise ValueError("Condição inválida. Use '>', '<', '==', '!=', '>=', '<='")

# 10 - Valores ausentes
def lidar_com_nan(df, estrategia='remover', valor=None):
    if estrategia == 'remover':
        return df.dropna()
    elif estrategia == 'preencher':
        return df.fillna(valor)
    else:
        raise ValueError("Estratégia inválida: use 'remover' ou 'preencher'")



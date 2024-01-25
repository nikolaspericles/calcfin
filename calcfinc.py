# **Trabalho Prático - Fundamentos de Programação para Ciência de Dados**

# Enunciado: Criar um Script em Python de calculadora financeira de juros compostos interativa capaz de calcular qualquer uma das variáveis da fórmula de juros compostos dadas as demais; Valor Final (vf), Capital Inicial (ci), Período (t) e Taxa (i).


# Script Trabalho Prático - Calculadora Juros Compostos

# Carregando os pacotes

from math import log # Carrega a função logaritmo

# Mensagem de Boas-vindas para o usuário

print("Bem-vindo(a) à calculadora de Juros Compostos!")

# A seguir, definiremos as funções de cálculo da calculadora de juros compostos:


# Esta função calcula o valor final, tendo como inputs o capital inicial, a taxa de juros e o número de períodos

def calc_vf(ci,i,t):

    vf = ci*(1+i)**t

    return vf


# Esta função calcula o valor inicial, tendo como inputs o valor final, a taxa de juros e o número de períodos

def calc_ci(vf,i,t):

    ci = vf/((1+i)**t)

    return ci


# Esta função calcula a taxa de juros, tendo como inputs o valor final, o valor inicial e o número de períodos

def calc_i(vf,ci,t):

    i = ((vf/ci)**(1/t))-1

    return i


# Esta função calcula o número de períodos, tendo como inputs o valor final, o valor inicial e a taxa de juros

def calc_t(vf,ci,i):

    t = log(vf/ci) / log(1+i)

    return t

# A seguir, realizaremos os cálculos solicitados:


# Variável base do loop que define se será realizado novo cálculo.
# Pare inicias os cálculos, o valor inicial definido é Sim (S)

continua_calculo = "S"

# Os cálculos serão realizados enquanto a variável continua_calculo for igual a Sim (S)
while continua_calculo == "S":

    # A variável tipo_calculo recebe do usuário o tipo de cálculo que será executado (vf, ci, t ou i)
    # A variável tipo_calculo é convertida para o tipo string e padronizada para minúscula, visando reduzir os erros de input

    tipo_calculo = str(input("O que você gostaria de calcular? (vf, ci, t, i): ")).lower()


    # Condição atendida caso o usuário escolha a opção de cálculo vf (definição do valor final)
    if tipo_calculo == "vf":
        ci = float(input("Insira o valor do Capital Inicial (ci): "))
        i = float(input("Insira o valor da Taxa (i): "))
        t = float(input("Insira o número de períodos (t): "))

        resultado = calc_vf(ci = ci,i = i,t = t)
        print(f"O valor final é igual a: {resultado:.2f}\n") # Variável resultado do tipo float, simplificada para 2 casas decimais.


    # Condição atendida caso o usuário escolha a opção de cálculo ci (definição do capital inicial)
    elif tipo_calculo == "ci":
        vf = float(input("Insira o Valor Final (vf): "))
        i = float(input("Insira o valor da Taxa (i): "))
        t = float(input("Insira o número de períodos (t): "))

        resultado = calc_ci(vf = vf,i = i,t = t)
        print(f"O capital inicial é igual a: {resultado:.2f}\n") # Variável resultado do tipo float, simplificada para 2 casas decimais.


    # Condição atendida caso o usuário escolha a opção de cálculo t (definição do número de períodos)
    elif tipo_calculo == "t":
        vf = float(input("Insira o Valor Final (vf): "))
        ci = float(input("Insira o valor do Capital Inicial (ci): "))
        i = float(input("Insira o valor da Taxa (i): "))

        resultado = calc_t(vf = vf,ci = ci,i = i)
        print(f"O período é igual a: {resultado:.2f}\n") # Variável resultado do tipo float, simplificada para 2 casas decimais.


    # Condição atendida caso o usuário escolha a opção de cálculo i (definição da taxa de juros)
    elif tipo_calculo == "i":
        vf = float(input("Insira o Valor Final (vf): "))
        ci = float(input("Insira o valor do Capital Inicial (ci): "))
        t = float(input("Insira o número de períodos (t): "))

        resultado = calc_i(vf = vf,ci = ci,t = t)
        print(f"A taxa de juros é igual a: {resultado:.2f}\n") # Variável resultado do tipo float, simplificada para 2 casas decimais.

    # Caso nenhuma das condições acima seja atendida, o usuário preencheu de forma incorreta e precisa digitar novamente.
    else:
        print("Tipo de cálculo não disponível. Tente novamente.\n")

    # Após as etapas acima, pergunta ao usuário se ele deseja continuar calculando.
    continua_calculo = str(input("Gostaria de realizar outro cálculo? (Digite S para sim e N para não).\n")).upper()

    # Trata o erro no caso do usuário responder diferente de sim (S) ou não (N).
    while continua_calculo != "S" and continua_calculo != "N":
      print("Valor inválido. Tente novamente.\n")
      continua_calculo = str(input("Gostaria de realizar outro cálculo? (Digite S para sim e N para não).\n")).upper()

    # Mensagem final caso o usuário não deseje continuar com os cálculos.
    if continua_calculo == "N":
      print("Se precisar fazer mais cálculos, volte a me executar.")


# Fim do script


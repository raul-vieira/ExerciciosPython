# 1.Faça um programa para imprimir: para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
def ex1(nInteiro):
    for i in range(0, nInteiro):
        print( str( nInteiro - (nInteiro - (i+1)))* (i+1))

# 2.Faça um programa para imprimir: para um n informado pelo usuário. Use uma função que receba um valor n inteiro e impr
def ex2(nInteiro):
    for i in range(1, nInteiro+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print(" ")

# 3. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
def ex3(x, y, z):
    print(x + y + z)
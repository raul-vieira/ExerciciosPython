# Ex. 1 Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
listaNumero = []
print("Informe 5 números")
for i in range(5):
    listaNumero.append(int(input("Número "+str(i+1)+":")))
print(listaNumero)

# Ex. 2 Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
listaNumero = []
print("Informe 10 números")
for i in range(10):
    listaNumero.append(int(input("Número " + str(i + 1) + ":")))
listaNumero.reverse()
print(listaNumero)

# Ex. 3 Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
listaNotas = []
print("Informe as 4 notas")
for i in range(4):
    listaNotas.append(float(input("Nota "+ str(i+1) + ":")))
mediaFinal = sum(listaNotas)/len(listaNotas)
if mediaFinal >= 7:
    print("Aluno Aprovado com média:" + str(mediaFinal))
else:
    print("Aluno Reprovado com média: " + str(mediaFinal))
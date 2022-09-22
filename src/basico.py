# Script básico para estudar algumas interações com Python
print("Ola Mundo!")
# Para executar o programa, digitar no prompt: python ./src/basico.py
nome = input("Qual o seu nome?")
print(f"Ola {nome}!")

# Programa para adivinhar o número secreto
from random import randint
# Gera número aleatório entre 1 e 10
numero_secreto = randint(1,10)
#Indica que o usuário ainda não acertou
acertou = False
#Repetição
while acertou != True:
    chute = int(input(f"{nome} informe um número:"))
    if chute == numero_secreto:
        acertou = True
    else:
        if chute > numero_secreto:
            print("Tente um número menor!")
        else:
            print("Tente um número maior!")
print("Parabens!")
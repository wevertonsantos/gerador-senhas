import random
'''
Gerador de senhas

1 - Usuário deve escolher tamanho da senha
2 - Quais caracteres deve ter na senha
'''

# 1 - pedido ao usuário
tamanho_senha = 10 #int(input("Digite o tamanho da senha: "))
incluir_maiusculas = "s" #input("Incluir letras maiúsculas? Digite 's' ou 'n'")
incluir_minusculas = "s" #input("Incluir letras minúsculas? Digite 's' ou 'n'")
incluir_numeros = "s" #input("Incluir números? Digite 's' ou 'n'")
incluir_simbolos = "s" #input("Incluir símbolos?? Digite 's' ou 'n'")

i = 0
x = 0
senha = ""
caracteres = []
maiusculas = ["A","W","C","G","D","P","L","K","D","S"]
minusculas = ["a","b","d","e","s","w","s","x","z","y"]
numeros = ["0","1","2","3","4","5","6","7","8","9"]
simbolos = ["!","@","$","%","&","-","*","+"]

#2 - fazer com que senha tenha o caractere pedido pelo usuário
if incluir_maiusculas == 's':
    caracteres += maiusculas 

if incluir_minusculas == 's':
    caracteres += minusculas

if incluir_numeros == 's':
    caracteres += numeros

if incluir_simbolos == 's':
    caracteres += simbolos

#3 - criar a senha do tamanho pedido pelo usuário
for i in range(tamanho_senha):
    senha += random.choice(caracteres)

print(senha)
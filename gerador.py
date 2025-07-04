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
senha = ""
lista_letras_maiusculas = ["A","W","C","G","D","P","L","K","D","S"]
lista_letras_minusculas = ["a","b","d","e","s","w","s","x","z","y"]
lista_simbolos = ["!","@","$","%","&","-","*","+"]

#2 - criar a senha do tamanho pedido pelo usuário
while i < tamanho_senha:
    i += 1

# 3 - adicionar numeros aleatorios na senha
if incluir_numeros == 's':
    senha += str(random.randint(0,9))
# 4 - letras maiusculas aleatorias na senha
if incluir_numeros == 's':
    senha += random.choice(lista_letras_maiusculas)
# 5 - letras minusculas aleatorias na senha
if incluir_numeros == 's':
    senha += random.choice(lista_letras_minusculas)
# 6 - simbolos aleatorios na senha
if incluir_numeros == 's':
    senha += random.choice(lista_simbolos)
print(senha)
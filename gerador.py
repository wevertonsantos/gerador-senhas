import random
'''
Gerador de senhas

1 - Usuário deve escolher tamanho da senha
2 - Quais caracteres deve ter na senha
'''

tamanho_senha = 12
lista_letras_maiusculas = ["A","B","C","D","E","F","W","X","Y","Z"]
lista_letras_minusculas = ["d","f","g","s","a","w","z","h","d","s"]
lista_numeros = []
for numero in range(0,50):
    lista_numeros.append(numero)
lista_simbolos = ["@","#","%","!","&","(","*","-"]

# pegar letras, numeros e simbolos até dar o tamanho da senha
letras_maiusculas = random.sample(lista_letras_maiusculas,5)
letras_minusculas = random.sample(lista_letras_minusculas,5)
simbolos = random.sample(lista_simbolos,5)
senha = []
#adicionado os caracteres na senha
senha += letras_maiusculas
senha += letras_minusculas
senha += simbolos
print(senha)
# criar a senha do tamanho pedido pelo usuário
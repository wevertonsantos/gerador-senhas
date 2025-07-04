import random
'''
Gerador de senhas

1 - Usuário deve escolher tamanho da senha
2 - Quais caracteres deve ter na senha
'''

def main():
    print("Gerador de senhas")
    tamanho_senha = int(input("Digite o tamanho da senha: "))
    letras_maiusculas = input("Incluir letras maiúsculas? Responda com 's' ou 'n' ")
    letras_minusculas = input("Incluir letras Incluir letras minúsculas? Responda com 's' ou 'n' ")
    incluir_numeros = input("Incluir números? Responda com 's' ou 'n' ")
    incluir_simbolos = input("Incluir símbolos? Responda com 's' ou 'n' ")

def criando_senha(tamanho_senha):
    lista_letras_maiusculas = ["A","B","C","D","E","F","W","X","Y","Z"]
    lista_letras_minusculas = ["d","f","g","s","a","w","z","h","d","s"]
    lista_numeros = []
    for numero in range(0,50):
        lista_numeros.append(numero)
    lista_simbolos = ["@","#","%","!","&","(","*","-"]
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
    ...
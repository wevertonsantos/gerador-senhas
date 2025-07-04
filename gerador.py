import random
'''
Gerador de senhas

1 - Usuário deve escolher tamanho da senha
2 - Quais caracteres deve ter na senha
'''

# 1 - pedir ao usuário o tamanho da senha
tamanho_senha = 12 #int(input("Digite o tamanho da senha: "))
#2 - criar a senha do tamanho pedido pelo usuário
i = 0
senha = ""
# 3 - letras maiusculas aleatorias na senha
lista_letras_maiusculas = ["A","W","C","G","D","P","L","K","D","S"]
letra_maiuscula = random.choice(lista_letras_maiusculas)
print(letra_maiuscula)
#while construindo a senha
while i < tamanho_senha:
    senha += str(i)
    i += 1
print(senha)
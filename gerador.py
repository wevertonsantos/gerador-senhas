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
lista_letras_maiusculas = ["A","W","C","G","D","P","L","K","D","S"]
#while construindo a senha
while i < tamanho_senha:
    # se tamanho da senha for igual tamanho passado pelo usuário
    if len(senha) == tamanho_senha:
        break
    else:
        # 3 - adicionar numeros aleatorios na senha
        senha += random.randint(0,50)
        # 4 - letras maiusculas aleatorias na senha
        senha += random.choice(lista_letras_maiusculas)
    i += 1
print(senha)
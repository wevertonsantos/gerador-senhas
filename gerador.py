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
lista_caracteres = ["A","W","C","G","D","P","L","K","D","S","a","b","d","e","s","w","s","x","z","y","!","@","$","%","&","-","*","+","0","1","2","3","4","5","6","7","8","9"]

#2 - criar a senha do tamanho pedido pelo usuário
for i in range(tamanho_senha):
    senha += random.choice(lista_caracteres)

    #senha.append(random.choice(lista_letras_maiusculas))
    #senha.append(random.choice(lista_letras_minusculas))
    #senha.append(str(random.randint(0,9)))
    #senha.append(random.choice(lista_simbolos))
# preciso fazer com que cada caractere entre no array e preencha ele por completo
print(senha)
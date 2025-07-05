import random
import string

# ponto de entrada principal do programa
def main():
    """
    função que coleta as preferências do usuário e exibe a senha gerada.
    """
    print("Gerador de Senhas Personalizadas")
    
    # entrada do usuário
    tamanho_senha = int(input("Digite o tamanho da senha: "))
    incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower()
    incluir_minusculas = input("Incluir letras minúsculas? (s/n): ").lower()
    incluir_numeros = input("Incluir números? (s/n): ").lower()
    incluir_simbolos = input("Incluir símbolos? (s/n): ").lower()

    # converte as entradas em valores booleanos (True/False)
    usar_maiusculas = incluir_maiusculas == 's'
    usar_minusculas = incluir_minusculas == 's'
    usar_numeros = incluir_numeros == 's'
    usar_simbolos = incluir_simbolos == 's'

    # chama a função para gerar a senha
    senha_gerada = gerar_senha(
        tamanho_senha,
        usar_maiusculas,
        usar_minusculas,
        usar_numeros,
        usar_simbolos
    )
    
    # exibe o resultado
    print(f"Senha gerada: {senha_gerada}")

# função responsável por montar a lista de caracteres disponíveis
def montar_lista_de_caracteres(usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos):
    """
    retorna uma lista de caracteres disponíveis para montar a senha, 
    com base nas opções escolhidas pelo usuário.
    """
    caracteres = []
    if usar_maiusculas:
        caracteres += list(string.ascii_uppercase)
    if usar_minusculas:
        caracteres += list(string.ascii_lowercase)
    if usar_numeros:
        caracteres += list(string.digits)
    if usar_simbolos:
        caracteres += list("!@#$%&*-+")
    return caracteres

# função principal para gerar a senha
def gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos):
    """
    gera uma senha aleatória com base no tamanho e nas categorias de caracteres selecionadas.
    """
    
    # monta a lista final de caracteres permitidos
    caracteres_possiveis = montar_lista_de_caracteres(
        usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos
    )

     # se o usuário não selecionou nenhuma categoria, não há como gerar senha
    if not caracteres_possiveis:
        return "Nenhum tipo de caractere selecionado!"

     # gera a senha com o tamanho desejado, escolhendo aleatoriamente da lista final
    senha = ''.join(random.choice(caracteres_possiveis) for _ in range(tamanho))
    return senha

main()
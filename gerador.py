import random
import string

# Ponto de entrada principal do programa
def main():
    """
    Função que coleta as preferências do usuário e exibe a senha gerada.
    """
    print("Gerador de Senhas Personalizadas")
    
    # Entrada do usuário
    tamanho_senha = int(input("Digite o tamanho da senha: "))
    incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower()
    incluir_minusculas = input("Incluir letras minúsculas? (s/n): ").lower()
    incluir_numeros = input("Incluir números? (s/n): ").lower()
    incluir_simbolos = input("Incluir símbolos? (s/n): ").lower()

    # Converte as entradas em valores booleanos (True/False)
    usar_maiusculas = incluir_maiusculas == 's'
    usar_minusculas = incluir_minusculas == 's'
    usar_numeros = incluir_numeros == 's'
    usar_simbolos = incluir_simbolos == 's'

    # Chama a função para gerar a senha
    senha_gerada = gerar_senha(
        tamanho_senha,
        usar_maiusculas,
        usar_minusculas,
        usar_numeros,
        usar_simbolos
    )
    
    # Exibe o resultado
    print(f"Senha gerada: {senha_gerada}")

# Função responsável por montar a lista de caracteres disponíveis
def montar_lista_de_caracteres(usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos):
    """
    Retorna uma lista de caracteres disponíveis para montar a senha, 
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

# Função principal para gerar a senha
def gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos):
    """
    Gera uma senha aleatória com base no tamanho e nas categorias de caracteres selecionadas.
    """
    
    # Monta a lista final de caracteres permitidos
    caracteres_possiveis = montar_lista_de_caracteres(
        usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos
    )

     # Se o usuário não selecionou nenhuma categoria, não há como gerar senha
    if not caracteres_possiveis:
        return "Nenhum tipo de caractere selecionado!"

     # Gera a senha com o tamanho desejado, escolhendo aleatoriamente da lista final
    senha = ''.join(random.choice(caracteres_possiveis) for _ in range(tamanho))
    return senha

main()
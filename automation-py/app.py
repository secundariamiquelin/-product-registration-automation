import pyautogui  # Automatiza o movimento do mouse do teclado e da digitação
from time import sleep  # importa a biblioteca "sleep" para dar uma pequena pausa na execução
import os  # Importa a biblioteca "os" para trabalhar com o sistema operacional

# 1- Clicar e digitar meu usuário
pyautogui.click(989, 547, duration=2)
pyautogui.write('jhonatan')

# 2 - Clicar e digitar a senha
pyautogui.click(959, 579, duration=2)
pyautogui.write("123456")

# 3 - Clicar em "Entrar"
pyautogui.click(811, 630, duration=2)

# Obtendo o caminho absoluto para o arquivo 'produtos.txt'
caminho_arquivo = os.path.abspath('produtos.txt')

# 4 - Extrair os produtos
with open(caminho_arquivo, 'r') as arquivo:
    print("Diretório Atual:", os.getcwd())  # Adiciona um print do diretório atual
    for linha in arquivo:
        produto, quantidade, preco = linha.strip().split(',')
        # 1 - Clicar e digitar o produto
        pyautogui.click(588, 525, duration=0.5)
        pyautogui.write(produto)
        # 2 - Clicar e digitar a quantidade
        pyautogui.click(560, 571, duration=0.5)
        pyautogui.write(quantidade)
        # 3 - Clicar e digitar o preço
        pyautogui.click(574, 603, duration=0.5)
        pyautogui.write(preco)
        # 4 - Clicar em registrar
        pyautogui.click(403, 846, duration=0.5)
        sleep(1)

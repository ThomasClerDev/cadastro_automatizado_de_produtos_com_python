import pyautogui
import openpyxl
import pyperclip

pyautogui.click(2292,386,duration=2)
# 2 - Abrir a planilha
workbook = openpyxl.load_workbook(r'C:\Users\tcler\Documents\cadastro_automatico_de_produtos_com_python\produtos.xlsx')
sheet_produtos = workbook['produtos']
for linha in sheet_produtos.iter_rows(min_row=2,max_row=501):
    produto = linha[0].value
    fornecedor = linha[1].value
    categoria = linha[2].value
    quantidade = linha[3].value
    valor_unitario = linha[4].value
    notificar_venda = linha[5].value
    # Colar dados campo produto
    pyautogui.click(2295,383, duration=0.5)
    pyautogui.write(produto)
    # Colar dados campo fornecedor
    pyautogui.click(2593,378, duration=0.5)
    pyautogui.write(fornecedor)
    # Colar dados campo categoria
    pyautogui.click(2297,477,duration=0.5)
    pyperclip.copy(categoria)
    pyautogui.hotkey('ctrl', 'v')
    # Colar dados campo Valor unitário
    pyautogui.click(2592,473,duration=0.5)
    pyperclip.copy(valor_unitario)
    pyautogui.hotkey('ctrl', 'v')
    # Se notificar venda for igual a sim, marcar sim
    # Se notificar venda for igual a não, marcar não
    if notificar_venda == 'Sim':
        pyautogui.click(2294,567,duration=0.5)
    elif notificar_venda == 'Não':
        pyautogui.click(2399,566,duration=0.5)
    # Clicar em registrar produto
    pyautogui.click(2399,641,duration=0.5)
    # Clicar em Ok na mensagem de cadastro com sucesso
    pyautogui.click(2739,171, duration=0.5)
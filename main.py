#Ainda testando o envio para o Git
import pyautogui
import time

# Para funcionar corretamente, o zoom precisa estar em 100%
# Página a ser copiada precisa estar aberta
# Arquivo Word a ser criado precisa estar em (x=1210, y=1170)

# Alterna abas antes de começar o código
pyautogui.keyDown('alt')
time.sleep(.2)
pyautogui.press('tab')
time.sleep(.2)
pyautogui.keyUp('alt')

time.sleep(1)

# ----------------------------------------------------------------------------------
# Inicia a automatização
# ----------------------------------------------------------------------------------

# colocar no loop o número pretendido de páginas
for i in range(17):
    # Expandir Navegador
    pyautogui.press('F11')
    time.sleep(0.5)

    # Click na tela para não correr o risco de perder o foco
    pyautogui.click(1000, 500)

    # Dá zoom em 175%
    pyautogui.keyDown('ctrl')
    pyautogui.press('+')
    pyautogui.press('+')
    pyautogui.press('+')
    pyautogui.press('+')
    pyautogui.keyUp('ctrl')

    # Seleciona e copia a página do livro
    pyautogui.hotkey('shift', 'winleft', 's')
    time.sleep(1)
    pyautogui.mouseDown(1120, 140, button='left')
    pyautogui.moveTo(1700, 900)
    pyautogui.mouseUp(1700, 900, button='left')
    time.sleep(1)

    #Mudar de página
    pyautogui.press('right')

    # Volta navegador ao normal para clicar no arquivo word
    pyautogui.press('F11')
    time.sleep(1)

    # Retorna zoom em 100%
    pyautogui.keyDown('ctrl')
    pyautogui.press('-')
    pyautogui.press('-')
    pyautogui.press('-')
    pyautogui.press('-')
    pyautogui.keyUp('ctrl')

    # Clica no arquivo word para selecioná-lo
    pyautogui.click(x=1210, y=1170)
    time.sleep(1)

    # Cola a página copiada do livro
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')

    # Pula uma linha para inserir a nova página copiada
    pyautogui.press('enter')
    time.sleep(1)

    # Retorna à página da Univesp
    time.sleep(1)
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')


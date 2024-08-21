# PESQUISA PNCP

import pyautogui
import pyperclip
import webbrowser
import time

# estado
estado = 'MG'

# Coloque as cidades
cidade1 = 'betim'
cidade2 = 'contagem'
cidade3 = 'juatuba'
cidade4 = 'igarape'
cidade5 = 'sarzedo'
cidade6 = 'São joaquim de bicas'
cidade7 = 'divinopolis'
cidade8 = 'para de minas'
cidade9 = 'sete lagoas'
cidade10 = 'ouro preto'
cidade11 = 'mario campos'
cidade12 = 'ibirite'
cidade13 = 'esmeraldas'
cidade14 = 'lagoa santa'
cidade15 = 'vespasiano'
cidade16 = 'itauna'
cidade17 = 'santa luzia'
cidade18 = 'congonhas'
cidade19 = 'conselheiro lafaiete'
cidade20 = 'itabira'
cidade21 = 'joao monlevade'
cidade22 = 'conceicao do mato dentro'
cidade23 = 'viçosa'
cidade24 = 'piranga'
cidade25 = 'barbacena'
cidade26 = 'são joao del rei'
cidade27 = 'nova serrana'
cidade28 = 'bom despacho'
cidade29 = 'lagoa da prata'
cidade30 = 'campo belo'

# abrir o navegador e ir para o site
webbrowser.open(
    'https://pncp.gov.br/app/editais?q=&status=recebendo_proposta&pagina=1')
time.sleep(1)

# configurando pausa de 5 segundos
pyautogui.PAUSE = 1

# clique e selecione dispensa
pyautogui.click(x=480, y=830)
pyautogui.click(x=320, y=610)
pyautogui.click(x=820, y=230)

# descendo a tela
pyautogui.click(x=1591, y=406)

# selecionando MG
pyautogui.click(x=485, y=400)
pyperclip.copy(estado)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

# clique e escreva as cidades
pyautogui.click(x=485, y=492)
pyperclip.copy(cidade1)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade2)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade3)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade4)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade5)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade6)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade7)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade8)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade9)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade10)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade11)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade12)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade13)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade14)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade15)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade16)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade17)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade18)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade19)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade20)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade21)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade22)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade23)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade24)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade25)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade26)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade27)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade28)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade29)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

pyautogui.click(x=485, y=492)
pyperclip.copy(cidade30)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(x=124, y=800)

# clicando em pesquisar
pyautogui.click(x=446, y=798)

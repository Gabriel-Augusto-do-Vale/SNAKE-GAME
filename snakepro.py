#TERMINAL: pip install pyautogui

import pyautogui
import time

pyautogui.keyDown('alt')
pyautogui.press(['tab'])
pyautogui.keyUp('alt')


repeticao = 0
#COMANDOS ANTES DA AUTOMATIZAÇÃO

pyautogui.press(['space'])
time.sleep(1.5)
pyautogui.press(['right'])
time.sleep(1.6)
pyautogui.press(['down'])
time.sleep(0.8)
pyautogui.press(['left'])
time.sleep (2.1)

###############################################

while repeticao < 50:
 pyautogui.press(['up'])
 pyautogui.press(['right'])
 time.sleep(1.96)


 #AUTOMATIZAÇÃO ESQUERDA DIREITA
 #
 ########################################


 pyautogui.press(['up'])
 pyautogui.press(['left'])
 time.sleep(1.958)
 pyautogui.press(['up'])
 pyautogui.press(['right'])
 time.sleep(1.958)

 #REPETIÇÃO ESQUERDA DIREITA
 pyautogui.press(['up'])
 pyautogui.press(['left'])
 time.sleep(1.958)
 pyautogui.press(['up'])
 pyautogui.press(['right'])
 time.sleep(1.958)
 pyautogui.press(['up'])
 pyautogui.press(['left'])
 time.sleep(1.958)
 pyautogui.press(['up'])
 pyautogui.press(['right'])
 time.sleep(1.958)
 pyautogui.press(['up'])
 pyautogui.press(['left'])
 time.sleep(1.958)
 pyautogui.press(['up'])





 #AUTOMATIZAÇÃO CIMA BAIXO

 time.sleep(0.65)
 pyautogui.press(['right'])
 pyautogui.press(['down'])
 time.sleep(0.616)
 pyautogui.press(['right'])
 pyautogui.press(['up'])
 time.sleep(0.596)
 pyautogui.press(['right'])
 pyautogui.press(['down'])
 time.sleep(0.617)


#REPETIÇÃO CIMA BAIXO

 pyautogui.press(['right'])
 pyautogui.press(['up'])
 time.sleep(0.595)
 pyautogui.press(['right'])
 pyautogui.press(['down'])
 time.sleep(0.615)
 pyautogui.press(['right'])
 pyautogui.press(['up'])
 time.sleep(0.595)
 pyautogui.press(['right'])
 pyautogui.press(['down'])
 time.sleep(0.615)
 pyautogui.press(['right'])
 pyautogui.press(['up'])
 time.sleep(0.595)
 pyautogui.press(['right'])


 #AUTOMATIZAÇÃO ESQUERDA DIREITA 2

 time.sleep(1)
 pyautogui.press(['down'])
 pyautogui.press(['left'])
 time.sleep(0.89)
 pyautogui.press(['down'])
 pyautogui.press(['right'])
 time.sleep(0.89)
 pyautogui.press(['down'])
 pyautogui.press(['left'])
 time.sleep(0.89)
 pyautogui.press(['down'])
 pyautogui.press(['right'])

 #CONTORNO

 pyautogui.press(['down'])
 pyautogui.press(['right'])
 pyautogui.press(['up'])
 pyautogui.press(['right'])
 pyautogui.press(['down'])
 pyautogui.press(['right'])
 pyautogui.press(['down'])
 pyautogui.press(['right'])
 pyautogui.press(['up'])
 pyautogui.press(['right'])
 pyautogui.press(['down'])
 pyautogui.press(['right'])
 pyautogui.press(['up'])
 pyautogui.press(['right'])
 pyautogui.press(['up'])
 pyautogui.press(['right'])
 pyautogui.press(['down'])
 time.sleep(1.32)
 pyautogui.press(['left'])
 time.sleep(2.1)

 repeticao = repeticao + 1

print ('acabou a repetiçao')




##################################################################

#FIM CICLO CO
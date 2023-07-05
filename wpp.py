from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui

#entrar no navegador e no site do wpp
janela = webdriver.Chrome()
janela.get('https://web.whatsapp.com/')
pyautogui.sleep (20)


janela.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys('Grupo')
pyautogui.sleep(2)
pyautogui.press('enter')
pyautogui.sleep(3)

janela.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys('oi pra vc')
pyautogui.sleep(3)
pyautogui.press('ENTER')
pyautogui.sleep(4)


janela.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys('Contato1')
pyautogui.sleep(2)
pyautogui.press('enter')
pyautogui.sleep(3)

janela.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys('Essa mensagem foi gerada automaticamente por 1 bot Angela')
pyautogui.sleep(3)
pyautogui.press('ENTER')
pyautogui.sleep(4)
                

quit






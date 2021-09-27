# importar as bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

# Navegar até o whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(15)
from selenium.webdriver.common.keys import Keys

# Definir o contato e mensagem
contatos = ["Princesa", "Cleiton"]
mensagem = 'Olá foi um prazer te conhecer!'
# Buscar contatos/grupos
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
    time.sleep(5)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)

# Campo de pesquisa 'copyable-text selectable-text'
# Campo de mensagem privada 'copyable-text selectable-text'

# Enviar mensagens p o contato/grupo
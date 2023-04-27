#Importando as libs
import pywhatkit
import keyboard
import time
from datetime import datetime

#Inserir contato
# contatos = ['+INSERIR CONTATO DESEJADO OU NOME DO GRUPO']


while len(contatos) >= 1:
    #Selecionando o contato, enviando a mensagem desejada no horário posto
    pywhatkit.sendwhatmsg(contatos[0],'Testando meu robô do whatsapp',datetime.now().hour, datetime.now().minute + 2)
    del contatos[0]#Deletando o contato
    time.sleep(120) #Tempo dado ao robô executar
    keyboard.press_and_release('ctrl + w') #Saindo da pagina
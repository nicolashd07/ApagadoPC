# Importar el módulo `telegram` y el módulo `os`
#python-telegram-bot

import telegram 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

# Crear una instancia del bot de Telegram
bot = telegram.Bot(token="")


def start(update, context):
  
  chat_id = update.effective_chat.id

  if chat_id ==462212154:
    bot.send_message(chat_id=chat_id, text="Usted cuenta con permisos para apagar y/o cancelar_apagado del sistema.")
  
  else:
    bot.send_message(chat_id=chat_id, text=f'El usuario {chat_id} no tiene permisos para apagar y/o cancelar_apagado del sistema. Pongase en contacto con el administrador')


# Definir la función que se ejecutará cuando se reciba el comando /apagar
def apagar(update, context):
 
  # Obtener el identificador del chat
  chat_id = update.effective_chat.id
  if chat_id == 462212154:
    #comando para apagar eequipo en 30s y guardarlo en la variable result
    result= os.system("shutdown -s -t 30")

    if result==0:
      print("El sistema se apagará en 30 segundos.")
      # Enviar el mensaje al usuario
      bot.send_message(chat_id=chat_id, text="Se apagará el sistema en 30 segundos.")

    elif result==1190:
      bot.send_message(chat_id=chat_id, text="Ya se programo un cierre de sistema.")

    else:
      bot.send_message(chat_id=chat_id, text=f'Favor de revisar en el log, codigo no reconocido ({result}.)')

  else:
    bot.send_message(chat_id=chat_id, text=f'El usuario no tiene permisos para apagar el sistema')
  

# Definir la función que se ejecutará cuando se reciba el comando /cancelar
def cancelar(update, context):
  #obtener el identificador de chat
  chat_id = update.effective_chat.id

  if chat_id ==462212154:
    # Cancelar el apagado del sistema
    result = os.system("shutdown -a")
    
    if result ==0:
      print('se ha cancelado el apagado del sistema.')
      bot.send_message(chat_id=chat_id, text='se ha cancelado el apagado del sistema.')

    elif result ==1116:
       bot.send_message(chat_id=chat_id, text='No se puede anular el apagado del sistema porque no se estaba apagando.')
      
    else: 
      bot.send_message(chat_id=chat_id, text=f'Favor de revisar en el log, codigo no reconocido ({result}.)')

  else: 
    bot.send_message(chat_id=chat_id, text='El usuario no tiene permiso para cancelar el apagado del sistema.')


# Crear un manejador para el comando /apagar
apagar_handler = telegram.ext.CommandHandler("apagar", apagar)

# Crear un manejador para el comando /cancelar
cancelar_handler = telegram.ext.CommandHandler("cancelar", cancelar)

#creamos un manejador con el comando /start que es el de bienvenida
start_handler = telegram.ext.CommandHandler('start', start)

# Crear una lista de manejadores
handlers = [apagar_handler, cancelar_handler,start_handler]

# Crear una instancia del updater
updater = telegram.ext.Updater(bot=bot)

# Añadir los manejadores a la instancia del updater
updater.dispatcher.add_handler(apagar_handler)
updater.dispatcher.add_handler(cancelar_handler)
updater.dispatcher.add_handler(start_handler)

# Iniciar el updater
updater.start_polling()
print('bot en linea')

# Ejecutar el updater indefinidamente
updater.idle()




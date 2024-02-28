from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import ChatPermissions

# Função para lidar com a entrada de novos membros
def welcome_message(update, context):
    # Nome do novo membro
    new_member = update.message.new_chat_members[0].first_name
    # Nome do grupo
    group_name = update.message.chat.title
    # Mensagem de boas-vindas personalizável
    welcome_text = f"Bem-vindo, {new_member}! 🎉\n\n{group_name} é um lugar incrível. Esperamos que você se sinta à vontade aqui!"

    # Enviar a mensagem de boas-vindas
    update.message.reply_text(welcome_text)

# Função para lidar com o comando /start
def start(update, context):
    update.message.reply_text("Olá! Eu sou o seu bot de boas-vindas personalizadas. Para configurar a mensagem de boas-vindas, use o comando /setwelcome <mensagem>.")

# Função para configurar a mensagem de boas-vindas
def set_welcome(update, context):
    if len(context.args) >= 1:
        # A primeira parte da mensagem após o comando /setwelcome será considerada a mensagem de boas-vindas
        welcome_message = ' '.join(context.args)
        context.chat_data['welcome_message'] = welcome_message
        update.message.reply_text("Mensagem de boas-vindas atualizada com sucesso!")
    else:
        update.message.reply_text("Por favor, insira uma mensagem de boas-vindas.")

def main():
    # Inicializando o updater do bot
    updater = Updater("6989042695:AAHxP_Rtw7AyhRwkVeHXFaIO0ChBKGBaGOM", use_context=True)

    # Obtendo o despachante para registrar os manipuladores
    dp = updater.dispatcher

    # Registrando o manipulador para lidar com a entrada de novos membros
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome_message))

    # Registrando o manipulador para o comando /start
    dp.add_handler(CommandHandler("start", start))

    # Registrando o manipulador para o comando /setwelcome
    dp.add_handler(CommandHandler("setwelcome", set_welcome, pass_args=True, pass_chat_data=True))

    # Iniciando o bot
    updater.start_polling()

    # Executando o bot até que Ctrl + C seja pressionado
    updater.idle()

if __name__ == '__main__':
    main()
  

from chatterbot import Chatbot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

for files in os.listdir('C:\Users\Stealth\Desktop\dist\ChatterBot-1.0.2\chatterbot-corpus-master\chatterbot_corpus\data\english'):
    data = open('C:\Users\Stealth\Desktop\dist\ChatterBot-1.0.2\chatterbot-corpus-master\chatterbot_corpus\data\english' + files , 'r').readline()
    bot.train(data)

while True:
    message = input('You:')
    if message.strip() != 'Bye':
        reply = bot.get_response(message)
        print('ChatBot :',reply)
    if message.strip() == 'Bye':
        print('ChatBot : Bye')
        break

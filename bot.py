import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = "Your Token"

def start(update,context):
	print(update)
	author = update.message.from_user.first_name
	#msg = update.message.text
	reply = "Hi {}".format(author)
	update.message.reply_text(reply)
	
	
def _help(update,context):
	help_txt = "Hey this is a help text"
	update.message.reply_text(help_txt)
	
	
def echo_text(update,context):
	reply = update.message.text
	update.message.reply_text(reply)
	
	
def echo_sticker(update,context):
	reply = update.message.sticker.file_id
	update.message.reply_sticker(reply)
	
	
def error(update,context):
	logger.error("Update '%s' caused error '%s'", update, context.error)
	

def main():
       updater = Updater(TOKEN, use_context=True)
	
       dp = updater.dispatcher
	
   
       dp.add_handler(CommandHandler("start",start))
       dp.add_handler(CommandHandler("help",_help))
       dp.add_handler(MessageHandler(Filters.text, echo_text))
       dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))
       dp.add_error_handler(error)
        
       updater.start_polling()
       logger.info("Started Polling...")
       updater.idle()

if __name__ == "__main__":
      main()
    
   

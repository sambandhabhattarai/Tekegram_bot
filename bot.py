import telebot
import datetime
import requests

# Define your bot token here
bot_token = '5935857573:AAFhE6iNHhUdgt2A72RJkI2oPBn1fgtrRd0'

# Create an instance of the bot
bot = telebot.TeleBot(bot_token)

# Define the '/start' command handler
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hi! I'm a chatbot. Type /help to see the list of available commands.")

# Define the '/help' command handler
@bot.message_handler(commands=['help'])
def help(message):
    response = """
    Here are the available commands:
    /start - Start the bot
    /help - Show the list of available commands
    /date - Show the current date
    /time - Show the current time
    /about - About the chatbot
    /quote - Get a random quote
    /fact - Get a random fact
    /joke - Get a random joke
    """
    bot.reply_to(message, response)

# Define the '/date' command handler
@bot.message_handler(commands=['date'])
def date(message):
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    bot.reply_to(message, date_str)

# Define the '/time' command handler
@bot.message_handler(commands=['time'])
def time(message):
    now = datetime.datetime.now()
    time_str = now.strftime("%H:%M:%S")
    bot.reply_to(message, time_str)

# Define the '/about' command handler
@bot.message_handler(commands=['about'])
def about(message):
    response = """
    I'm a chatbot created by Sambandha Bhattarai. 
    My purpose is to provide helpful information and assistance.
    """
    bot.reply_to(message, response)

# Define the '/quote' command handler
@bot.message_handler(commands=['quote'])
def quote(message):
    response = requests.get("https://api.quotable.io/random").json()
    quote_str = f"{response['content']} - {response['author']}"
    bot.reply_to(message, quote_str)

# Define the '/fact' command handler
@bot.message_handler(commands=['fact'])
def fact(message):
    response = requests.get("https://useless-facts.sameerkumar.website/api").json()
    fact_str = response['data']
    bot.reply_to(message, fact_str)

# Define the '/joke' command handler
@bot.message_handler(commands=['joke'])
def joke(message):
    response = requests.get("https://official-joke-api.appspot.com/random_joke").json()
    joke_str = f"{response['setup']} \n\n{response['punchline']}"
    bot.reply_to(message, joke_str)
    

# Start the bot
bot.polling()

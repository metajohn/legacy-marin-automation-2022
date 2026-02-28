import telebot
import os

bot = telebot.TeleBot(os.environ['TELEGRAM_BOT_KEY'])



def notifyOfStall(causeOfProblem):
    bot.send_message(os.environ['TELEGRAM_PHONEN_ME'], causeOfProblem)

def notifyOfCompletion(whatHasCompleted):
    bot.send_message(os.environ['TELEGRAM_PHONEN_ME'], whatHasCompleted)
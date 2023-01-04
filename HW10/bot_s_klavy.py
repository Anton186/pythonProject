from bot_token import *
import logging


from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

reply_keyboard = [['/play', '/settings'],
                  ['/rules', '/close']]

candies = 2021
step = 37
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
TOKEN = token


def start(update, context):
    name = f"{update.message.from_user.first_name} {update.message.from_user.last_name}"
    update.message.reply_text(
        f"Привет, {name}!   Давай поиграем в игру\n - Забери конфеты!!!\n Чтобы узнать"
        " правила игры или играем - нажми клавишу :",
        reply_markup=markup
    )


def close_keyboard(update, context):
    update.message.reply_text(
        "Ok \U0001F606",
        reply_markup=ReplyKeyboardRemove()
    )


def rules(update, context):
    update.message.reply_text(
        "В начале игры нужно определить количество конфет на кону и количество конфет, "
        "которое можно взять за один раз кнопка - /settings")


def settings(update, context):
    update.message.reply_text("Введите количество конфет на кону и максимально "
                              "возможное количество на ход через пробел:")
    return 1


def set_settings(update, context):
    global candies
    global step
    candies, step = map(int, update.message.text.split())
    update.message.reply_text("Правила установлены, начинаем!", reply_markup=markup)
    return ConversationHandler.END


def play(update, context):
    update.message.reply_text(f"На кону {candies} конфет. Ваш ход. Какое количество конфет вы берете?"
                              f"(Максимальное = {step} )", reply_markup=ReplyKeyboardRemove())
    return 1


def play_step(update, context):
    global candies
    candiy = int(update.message.text)
    candies -= candiy
    if candies <= step:
        update.message.reply_text("Игра окончена. Я забираю оставшиеся конфеты, я победил!", reply_markup=markup)
        return ConversationHandler.END
    else:
        update.message.reply_text(f"На кону {candies} конфет, я беру {candies % (step + 1)}")
        candies -= candies % (step + 1)
        if candies <= step:
            update.message.reply_text("Поздравляю, ты победил!!!", reply_markup=markup)
            return ConversationHandler.END


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    settings_hundler = ConversationHandler(
        entry_points=[CommandHandler('settings', settings)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, set_settings)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    play_hundler = ConversationHandler(
        entry_points=[CommandHandler('play', play)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, play_step)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(settings_hundler)
    dp.add_handler(play_hundler)

    dp.add_handler(CommandHandler("close", close_keyboard))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
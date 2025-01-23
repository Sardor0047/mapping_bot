import os
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from telegram import ReplyKeyboardMarkup
from members_info import gayrat,alirizo,zafar,mirzo,kafolat,negaEurope,qandeyMashinalar,manzil
from kia import *
from hyundai import *
from chevralet import *

def start(update, context):
    keyboard = [
        ['Servisimiz Haqida'],
        ["Gaz o'rnatish"]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard)

    update.message.reply_text(
        "Assalomu alaykum! EuropeGas botiga xush kelibsiz! 🏠💨\n\n"
        "Sizni qanday yordam kerak?\n\n"
        "Iltimos, menyudan biror xizmatni tanlang:\n\n"
        "1️⃣ Servisimiz haqida\n"
        "2️⃣ Gaz o'/'rnatish\n\n",
        reply_markup=reply_markup  # reply_markup bu yerda tugmalarni ko'rsatadi
    )


def service(update,context):
    keyboard = [
        ["Servisimiz Faoliyati","EuropeGas Oila Azolari"],
        ["Manzil","/start"]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard)

    update.message.reply_text(
        "Servisimiz Faoliyati\n\n"
        "EuropeGas Oila Azolari\n\n"
        'Manzil',reply_markup=reply_markup
    )



def faoliyat(update,context):
        keyboard = [
             ["EuropeGas nimalarga kafolat beradi ?","Qancha mashinalarga gaz qo'ygan va qandey moshinalarga o'rnata oladi?"],
             ["Nima uchun EuropeGasni tanlash kerak?","Servisimiz Haqida"],
        ]

        reply_markup = ReplyKeyboardMarkup(keyboard)

        update.message.reply_text(
             "Biz haqimizda !",
             reply_markup=reply_markup
        )


def oila_azolar(update,context):
     keyboard = [
          ["Sotuvchilar"],
          ["Ustolar"]
     ]

     reply_markup = ReplyKeyboardMarkup(keyboard)

     update.message.reply_text(
          "Oila a'zolarimi :",
          reply_markup=reply_markup
     )

def sotuvchilar(update,context):
     keyboard = [
          ["Zafar"],
          ["Mirzo"],
          ["EuropeGas Oila Azolari"]
     ]

     reply_markup = ReplyKeyboardMarkup(keyboard)
     update.message.reply_text(
          "Sotuvchilarimiz !",
          reply_markup=reply_markup
     )

def ustolar(update,context):
     keyboard = [
          ['Alirizo'],
          ["G'ayrat"],
          ["EuropeGas Oila Azolari"]
     ]

     reply_markup = ReplyKeyboardMarkup(keyboard)

     update.message.reply_text(
          "Ustolarimiz !",
          reply_markup = reply_markup
     )


def gaz_ornatish(update,context):
     keyboard = [
          ['Chevralet'],
          ['Hyundai'],
          ['Kia'],
          ['/start']
     ]

     reply_markup = ReplyKeyboardMarkup(keyboard)

     update.message.reply_text(
          "Avtamobil turini tanlang",
          reply_markup=reply_markup
     )

def chevralet(update,context):
     keyboard = [
          ["Nexia 2","Nexia 3"],
          ["Gentra", "Cobalt"],
          ["Tracer(Uzb)","Onix"],
          ["Monza",],["Equinox 1/2"],
          ["Malibu 2", "Malibu 1"],
          ["⬅️ moshina turi"]
     ]

     reply_markup = ReplyKeyboardMarkup(keyboard)
     update.message.reply_text(
          "Chevralet avtamabil turini tanlang",
          reply_markup=reply_markup
     )

def kia(update,context):
    keyboard = [
          ["K5","K8"],
          ["K9", "Sorento"],
          ["Sportage","EV6"],
          ["Carnival",],["Bongo"],
          ["Sonet", "Cerato"],
          ["⬅️ moshina turi"]
     ]

    reply_markup = ReplyKeyboardMarkup(keyboard)
    update.message.reply_text(
          "Kia avtamabil turini tanlang",
          reply_markup=reply_markup
     )
def hyundai(update,context):
    keyboard = [
          ["Elantra","Sonata"],
          ["Tucson", "Palisade"],
          ["⬅️ moshina turi"]
     ]

    reply_markup = ReplyKeyboardMarkup(keyboard)
    update.message.reply_text(
          "Hyundai avtamabil turini tanlang",
          reply_markup=reply_markup
     )


Token = os.getenv('TOKEN')



updater = Updater(token=Token)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start',start))
dispatcher.add_handler(MessageHandler(Filters.text('Servisimiz Haqida'),callback= service))
dispatcher.add_handler(MessageHandler(Filters.text("Servisimiz Faoliyati"),callback= faoliyat))

dispatcher.add_handler(MessageHandler(Filters.text("EuropeGas nimalarga kafolat beradi ?"),callback= kafolat))
dispatcher.add_handler(MessageHandler(Filters.text("Qancha mashinalarga gaz qo'ygan va qandey moshinalarga o'rnata oladi?"),callback= qandeyMashinalar))
dispatcher.add_handler(MessageHandler(Filters.text("Nima uchun EuropeGasni tanlash kerak?"),callback= negaEurope))

dispatcher.add_handler(MessageHandler(Filters.text("Manzil"),callback= manzil))

dispatcher.add_handler(MessageHandler(Filters.text('EuropeGas Oila Azolari'),callback= oila_azolar))

dispatcher.add_handler(MessageHandler(Filters.text('Sotuvchilar'),callback= sotuvchilar))
dispatcher.add_handler(MessageHandler(Filters.text("Ustolar"),callback= ustolar))
dispatcher.add_handler(MessageHandler(Filters.text('Zafar'),callback= zafar))
dispatcher.add_handler(MessageHandler(Filters.text('Mirzo'),callback= mirzo))
dispatcher.add_handler(MessageHandler(Filters.text('Alirizo'),callback= alirizo))
dispatcher.add_handler(MessageHandler(Filters.text("G'ayrat"),callback= gayrat))


dispatcher.add_handler(MessageHandler(Filters.text("Gaz o'rnatish"),callback= gaz_ornatish))

dispatcher.add_handler(MessageHandler(Filters.text("Kia"),callback= kia))

dispatcher.add_handler(MessageHandler(Filters.text("K5"),callback= k5))
dispatcher.add_handler(MessageHandler(Filters.text("K8"),callback= k8))
dispatcher.add_handler(MessageHandler(Filters.text("K9"),callback= k9))
dispatcher.add_handler(MessageHandler(Filters.text("Sorento"),callback= sorento))
dispatcher.add_handler(MessageHandler(Filters.text("Sportage"),callback= sportage))
dispatcher.add_handler(MessageHandler(Filters.text("Carnival"),callback= carnival))
dispatcher.add_handler(MessageHandler(Filters.text("Bongo"),callback= Bongo))
dispatcher.add_handler(MessageHandler(Filters.text("Sonet"),callback= sonet))
dispatcher.add_handler(MessageHandler(Filters.text("Cerato"),callback= Cerato))
dispatcher.add_handler(MessageHandler(Filters.text("EV6"),callback= EV6))

dispatcher.add_handler(MessageHandler(Filters.text("Hyundai"),callback= hyundai))

dispatcher.add_handler(MessageHandler(Filters.text("Elantra"),callback= elantra))
dispatcher.add_handler(MessageHandler(Filters.text("Sonata"),callback= sonata))
dispatcher.add_handler(MessageHandler(Filters.text("Tucson"),callback= Tucson))
dispatcher.add_handler(MessageHandler(Filters.text("Palisade"),callback= Palisade))
dispatcher.add_handler(MessageHandler(Filters.text("⬅️ moshina turi"),callback= gaz_ornatish))

dispatcher.add_handler(MessageHandler(Filters.text("Chevralet"),callback= chevralet))

dispatcher.add_handler(MessageHandler(Filters.text("Nexia 2"),callback= Nexia2))
dispatcher.add_handler(MessageHandler(Filters.text("Nexia 3"),callback= Nexia3))
dispatcher.add_handler(MessageHandler(Filters.text("Gentra"),callback= gentra))
dispatcher.add_handler(MessageHandler(Filters.text("Cobalt"),callback= cobalt))
dispatcher.add_handler(MessageHandler(Filters.text("Tracer(Uzb"),callback= tracer))
dispatcher.add_handler(MessageHandler(Filters.text("Onix"),callback= onix))
dispatcher.add_handler(MessageHandler(Filters.text("Monza"),callback= monza))
dispatcher.add_handler(MessageHandler(Filters.text("Equinox 1/2"),callback= equinox1_2))
dispatcher.add_handler(MessageHandler(Filters.text("Malibu 2"),callback= malibu2))
dispatcher.add_handler(MessageHandler(Filters.text("Malibu 1"),callback= malibu1))

updater.start_polling()
updater.idle()
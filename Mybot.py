import telebot
import mysql.connector

import mytoken

from datetime import date
from datetime import datetime
TOKEN=mytoken.TOKEN
myBot = telebot.TeleBot(TOKEN)
myDb=mysql.connector.connect(host='localhost',user='root',database='db_api')
from telebot import apihelper
sql=myDb.cursor()
waktusekarang=datetime.now()
class Mybot:
    def __init__(self):
        self.message

    @myBot.message_handler(commands=['start', 'help'])
    def start(message):
        teks = mytoken.SAPA + "\n Siswa XI RPL 2  - SMK Taruna Bhakti \U0001F984 "+"\n" \
                        "  hari ini tanggal "+str(waktusekarang)
        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['datasiswa'])
    def menu_data_siswa(message):
        query="select nipd,nama,kelas from tabel_siswa "
        sql.execute(query)
        data=sql.fetchall()
        jmldata = sql.rowcount
        kumpuldata = ''
        if (jmldata > 0):
            # print(data)
            no = 0
            for x in data:
                no += 1
                kumpuldata = kumpuldata + str(x) + '\n'
                print(kumpuldata)
                kumpuldata = kumpuldata.replace('(', '')
                kumpuldata = kumpuldata.replace(')', '')
                kumpuldata = kumpuldata.replace("'", '')
                kumpuldata = kumpuldata.replace(",", '')
        else:
            print('data kosong')

        myBot.reply_to(message,str(kumpuldata))
            
print(myDb)
print("-- Bot sedang berjalan --")
myBot.polling(none_stop=True)
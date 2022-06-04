
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ( CommandHandler, Filters, MessageHandler, Updater)
from message import Editmessage, Sendmessage, logger
import os
import telepot
import urllib.request
from PIL import Image
import requests
from bs4 import BeautifulSoup
import random
import string
import time
import json
import math, string
dia='✅'

os.environ['TZ'] = 'America/Buenos_Aires'

gods=["21951A6626","21951A6637","21951A6627","21951A6614"]
members = [2141450636,809309749,2045746007,1257359605,2113380774]
bot_token = os.environ.get('TG_BOT_TOKEN')
startmessage = [[
		InlineKeyboardButton(
			"Dev",
			url='https://t.me/dheeraj2324'
		),
        InlineKeyboardButton(
			"Channel",
			url='https://t.me/aboutdheeraj'
		)
        ]]


def start(update, context):
    info = update.effective_user
    print(info)
    chat_id = info.id
    print(chat_id)
    userid= info['username']
    text = f'Welcome @{userid}, to maths calculator bot and also private stuff dev has no relation to this, to know more use /help  This bot is provided for educational use!! , ENTER IN YOUR OWN RISK!!!!!!! . YOU ARE RESPONSIBLE FOR YOUR OWN ACTION!.'
    Sendmessage(chat_id, text, reply_markup=InlineKeyboardMarkup(startmessage))
    return
def help(update, context):
    chat_id = update.message.chat_id
    text = "Available cmds available:\n /cal \n /add \n /sub \n /multiply \n /divide \n secrect cmds are onlY shared with known!!  ENTER IN YOUR OWN RISK!!!!!!!!"
    Sendmessage(chat_id, text, reply_markup= InlineKeyboardMarkup(startmessage))
def botcmds(update, context):
    chat_id = update.message.chat_id
    text = "Hey, welcome to this Bot! sorry to say cmds of the bots have been taken to private!!"
    Sendmessage(chat_id, text)

def ssc(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    global members
    text =  update.message.text.split(' ',1)
    tempp=text[-1]
    logger.info(text)
    print(info)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:		
            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_SSC.jpg".format(textt,textt)
            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
            payload = {
                "chat_id" : chat_id,
                "photo" : photos,
                "caption" : "✅ Done!!"
            }
            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
            res=requests.post(to_url , data=payload)
    else:
        text = "Gods do not permit your entry!"
        Sendmessage(chat_id,text)
def fssc(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    global members
    text =  update.message.text.split(' ',1)
    tempp=text[-1]
    logger.info(text)
    print(info)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:		
            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/IARE/STAFF/{}/DOC/{}_SSC.jpg".format(textt,textt)
            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
            payload = {
                "chat_id" : chat_id,
                "photo" : photos,
                "caption" : "✅ Done!!"
            }
            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
            res=requests.post(to_url , data=payload)
    else:
        text = "Gods do not permit your entry!"
        Sendmessage(chat_id,text)
def fpan(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    global members
    text =  update.message.text.split(' ',1)
    tempp=text[-1]
    logger.info(text)
    print(info)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:		
            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/IARE/STAFF/{}/DOC/{}_PAN_CARD.jpg".format(textt,textt)
            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
            payload = {
                "chat_id" : chat_id,
                "photo" : photos,
                "caption" : "✅ Done!!"
            }
            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
            res=requests.post(to_url , data=payload)
    else:
        text = "Gods do not permit your entry!"
        Sendmessage(chat_id,text)
def addgod(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    global members
    print(info)
    logger.info(text)
    text =  update.message.text.split(' ',1)
    if chat_id in members:
        tempp=text[-1]
        global gods
        textt=tempp.upper()
        gods.append(textt)
        text = "Done!"
        Sendmessage(chat_id,text)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
#############################################################################################################################################
def inter(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    global members
    text =  update.message.text.split(' ',1)
    tempp=text[-1]
    print(info)
    logger.info(text)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:		
            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_INTER.jpg".format(textt,textt)
            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
            payload = {
                "chat_id" : chat_id,
                "photo" : photos,
                "caption" : "✅ Done!!"
            }
            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
            res=requests.post(to_url , data=payload)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
def finter(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    text =  update.message.text.split(' ',1)
    global members
    tempp=text[-1]
    print(info)
    logger.info(text)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:		
            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/IARE/STAFF/{}/DOC/{}_INTER.jpg".format(textt,textt)
            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
            payload = {
                "chat_id" : chat_id,
                "photo" : photos,
                "caption" : "✅ Done!!"
            }
            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
            res=requests.post(to_url , data=payload)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
def pic(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    text =  update.message.text.split(' ',1)
    tempp=text[-1]
    logger.info(text)
    global members
    print(info)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods can't be seen!!"
            Sendmessage(chat_id,text)
        else:		
            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/{}.jpg".format(textt,textt)
            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
            payload = {
                "chat_id" : chat_id,
                "photo" : photos,
                "caption" : "✅ Done!!"
            }
            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
            res=requests.post(to_url , data=payload)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
def fpic(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    text =  update.message.text.split(' ',1)
    tempp=text[-1]
    logger.info(text)
    global members
    print(info)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods cann't be seen!!"
            Sendmessage(chat_id,text)
        else:		
            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/IARE/STAFF/{}/DOC/{}_PHOTO.jpg".format(textt,textt)
            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
            payload = {
                "chat_id" : chat_id,
                "photo" : photos,
                "caption" : "✅ Done!!"
            }
            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
            res=requests.post(to_url , data=payload)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
################################################################################################################################
def bd(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    global members
    text =  update.message.text.split(' ',1)
    tempp=text[-1]
    logger.info(text)
    print(info)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:		
            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_BIRTHCERTIFICATE.jpg".format(textt,textt)
            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
            payload = {
                "chat_id" : chat_id,
                "photo" : photos,
                "caption" : "✅ Done!!"
            }
            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
            res=requests.post(to_url , data=payload)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
################################################################################################################################################
def aadhar(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    global members
    userid= info['username']
    text =  update.message.text.split(' ',1)
    tempp=text[-1]
    logger.info(text)
    print(info)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:		
            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_Aadhar.jpg".format(textt,textt)
            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
            payload = {
                "chat_id" : chat_id,
                "photo" : photos,
                "caption" : "✅ Done!!"
            }
            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
            res=requests.post(to_url , data=payload)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
	
def all_details(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    if chat_id in members:
        funcs = [pic, aadhar, ssc, inter, bd, eamcet, caste, income]
        for i in funcs:
            try: i(update, context)
            except: pass
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
	
def picture_in_range(update, context):
	
    global bot_token
	
    chat_id = update.message.chat_id
    info = update.effective_user
    global members
    userid= info['username']
    text =  update.message.text.split(' ',1)
    #tempp=text[-1]
    #logger.info(text)
    #print(info)
    #textt=tempp.upper()

    upper_lim = text[-1].upper()
    lower_lim = text[-2].upper()
    base = text[-3].upper()
    gender = text[-4].upper()

    Sendmessage(chat_id, " ".join([upper_lim, lower_lim, base, gender]))
    
    if any(c.isalpha() for c in upper_lim) and any(c.isalpha() for c in lower_lim):
	a1, n1 = lower_lim[0], int(lower_lim[1])
	a2, n2 = upper_lim[0], int(upper_lim[1])
	all_caps = list(string.ascii_uppercase)
	if a1 >= a2:
		Sendmessage(chat_id,"Invalid range!")
		return None
	while a1 <= a2:
		while n1 <= 9:
			rno = base + a1 + str(n1)
			#send pic logic generalised
			photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/{}.jpg".format(rno,rno)
			payload = {
				"chat_id" : chat_id,
				"photo" : photos,
				"caption" : "✅ Done!!"
			    }
			to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
            		res=requests.post(to_url , data=payload)
			n1 += 1
		else:
			n1 = 0
			a1 = all_caps[ all_caps.index(a1) + 1 ]
			
    elif not(any(c.isalpha() for c in upper_lim) or any(c.isalpha() for c in lower_lim)):
	
	n1, n2 = int(lower_lim), int(upper_lim)
	if n1 >= n2:
		Sendmessage(chat_id, "Invalid range; Syntax: /picrange gender base lowerlimit upperlimit")
	while n1 <= n2:
		if len(str(n1)) == 1:
			ton1 = "0" + str(n1)
		else:
			ton1 = str(n1)
		rno = base + ton1
		photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/{}.jpg".format(rno,rno)
		payload = {
			"chat_id" : chat_id,
			"photo" : photos,
			"caption" : "✅ Done!!"
		    }
		to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
		res=requests.post(to_url , data=payload)
		n1 += 1
	
def faadhar(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    text =  update.message.text.split(' ',1)
    global members
    tempp=text[-1]
    logger.info(text)
    print(info)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:		
            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/IARE/STAFF/{}/DOC/{}_AADHAR_CARD.jpg".format(textt,textt)
            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
            payload = {
                "chat_id" : chat_id,
                "photo" : photos,
                "caption" : "✅ Done!!"
            }
            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
            res=requests.post(to_url , data=payload)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
##########################################################################################################################################################
def eamcet(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    text =  update.message.text.split(' ',1)
    global members
    tempp=text[-1]
    logger.info(text)
    print(info)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:
            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_EAMCET_RANK.jpg".format(textt,textt)
            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
            payload = {
                "chat_id" : chat_id,
                "photo" : photos,
                "caption" : "✅ Done!!"
            }
            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
            res=requests.post(to_url , data=payload)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
def caste(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    global members
    text =  update.message.text.split(' ',1)
    tempp=text[-1]
    logger.info(text)
    print(info)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:
            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_Caste.jpg".format(textt,textt)
            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
            payload = {
                "chat_id" : chat_id,
                "photo" : photos,
                "caption" : "✅ Done!!"
            }
            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
            res=requests.post(to_url , data=payload)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
def income(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    global members
    text =  update.message.text.split(' ',1)
    tempp=text[-1]
    logger.info(text)
    print(info)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:
            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_Income.jpg".format(textt,textt)
            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
            payload = {
                "chat_id" : chat_id,
                "photo" : photos,
                "caption" : "✅ Done!!"
            }
            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
            res=requests.post(to_url , data=payload)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
#####################################################################################################################################################################


def main():
    updater = Updater(
        bot_token,
        use_context=True
    )
    dp = updater.dispatcher
    #dp.add_handler(MessageHandler(Filters.text & ~Filters.command, duty))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("pic", pic))
    dp.add_handler(CommandHandler("Pic", pic))
    dp.add_handler(CommandHandler("income", income))
    dp.add_handler(CommandHandler("Income", income))
    dp.add_handler(CommandHandler("caste", caste))
    dp.add_handler(CommandHandler("Caste", caste))
    dp.add_handler(CommandHandler("inter", inter))
    dp.add_handler(CommandHandler("aadhar", aadhar))
    dp.add_handler(CommandHandler("all", all_details))
    dp.add_handler(CommandHandler("eamcet", eamcet))
    dp.add_handler(CommandHandler("bd", bd))
    dp.add_handler(CommandHandler("addgod", addgod))
    dp.add_handler(CommandHandler("Aadhar", aadhar))
    dp.add_handler(CommandHandler("botcmds", botcmds))
    dp.add_handler(CommandHandler("ssc", ssc))
    dp.add_handler(CommandHandler("fssc", fssc))
    dp.add_handler(CommandHandler("finter", finter))
    dp.add_handler(CommandHandler("fpan", fpan))
    dp.add_handler(CommandHandler("fpic", fpic))
    dp.add_handler(CommandHandler("faadhar", faadhar))
    dp.add_handler(CommandHandler("picrange", picture_in_range))
    logger.info("Bot Started!!!")
    updater.start_polling()
    updater.idle()
if __name__ == "__main__":
    main()

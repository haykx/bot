from main import telegram_chatbot
import random

bot = telegram_chatbot()

def make_reply(msg):
    
    if msg[0]!='/':
        msg=str(msg)
        msg=msg.lower()
        msg=msg.replace(' ','')
        arr=['rock','paper','scissors']
        arrr=['r','p','s']
        f=random.randint(0,2)
        g=arr[f]
        if msg=='r' and g=='scissors':
            reply=g+'. You won!'
        elif msg=='p' and g=='rock':
            reply=g+'. You won!'
        elif msg=='s' and g=='paper':
            reply=g+'. You won!'
        elif msg=='r' and g=='rock':
            reply = g + '. Tie'
        elif msg=='p' and g=='paper':
            reply = g + '. Tie'
        elif msg=='s' and g=='scissors':
            reply = g + '. Tie'
        else:
            if msg in arrr:
                reply = g+'. You lost HAHAHAHAHAHA!'
            elif msg not in arrr:
                reply = 'please enter r,p or s'
    else:
        if msg=='/start':
            reply='Hello!\nLets play some rock, parer, scissors shall we?!\nSo how it works?\nYou should enter r for rock, p for paper and s for scissors.\nGood luck!'
        else:
            reply='iNvAlId CoMmAnD LOL'
    return reply

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            ggg = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, ggg)
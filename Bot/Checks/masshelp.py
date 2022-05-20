
    #############################################################
import requests
from message import logger, Sendmessage, Editmessage, logger
from datetime import date
import time

def mass_helper(chat_id ,combo):

    status = Sendmessage(chat_id, '<i>Checking....</i>')
    tic = time.perf_counter()
    wdia ='❌'
    crs = '➟'
    dia='✅'
    try:
        i=combo.split("|")
        cc=i[0]
        skq1=sk_chg[:16]
        skq2="x"*78
        skq3=sk_chg[-4:]
        skmains=(skq1+skq2+skq3)
        mes=i[1]
        ano=i[2]
        cvv=i[3]
        url = 'https://api.stripe.com/v1/payment_methods'
        headers = {
        'Authorization': 'Bearer' + " " +sk_chg,
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'type': 'card',
            'card[number]': i[0],
            'card[exp_month]': i[1],
            'card[exp_year]': i[2],
            'card[cvc]': i[3]
        }
        response = requests.post(url, headers=headers, data=data)
        q=response.text
        w=json.loads(q)
        if "testmode_charges_only" in response.text:
            text = (f"""
    {wdia} SK-key expired {crs} Change SK key \n Sk-key {crs} <code>{skmains}</code> \n RESPONSE {crs} Testmode Charges Only \n ━━━━━━━━━━━━━━━ \n CHECKED BY @ASURCCWORLDBOT \n Used by @{userid}
    """)
            Editmessage(chat_id, text, status)
        if "error" in w:
            text = (f"""
{wdia} Error {crs} {w["error"]["code"]} \n  ━━━━━━━━━━━━━━━ \n CHECKED BY @ASURCCWORLDBOT \n Used by @{userid}
""")
#Response {crs} {w["error"]["decline_code"]}
            Editmessage(chat_id, text, status)
        else:
        #second request
            url = 'https://api.stripe.com/v1/payment_intents'
            headers = {
            'Authorization': 'Bearer' + " " +sk_chg,
            'Content-Type': 'application/x-www-form-urlencoded'
            }
            data = {
                'amount':  '60' ,
                'currency': 'usd',
                'payment_method_types[]': 'card',
                'description': 'Asur Donation',
                'payment_method': w["id"],
                'confirm': 'true',
                'off_session': 'true'
            }
            response = requests.post(url, headers=headers, data=data)
            b=response.text
            e=json.loads(b)
            if "error" not in e:
                msg = "CCN or CVV LIVE!"
            else:
                msg = e["error"]["message"]
            toc = time.perf_counter()
            if 'card' in w:
                if w['card']['three_d_secure_usage']['supported'] == True:
                    vs ="False ✅"
                else:
                    vs="True ❌"
            else:
                vs="True ❌"
            if "incorrect_cvc" in b:
                text = (f"""
{dia} CC {crs} <code>{cc[:7]}xxxxxxxxxx|{mes}|{ano}|{cvv}</code>
STATUS {crs} #ApprovedCCN
MSG {crs} {msg}
VBV[3D] {crs} {vs}
TOOK: {toc - tic:0.4f}s 
CHECKED BY @ASURCCWORLDBOT
Used by @{userid}
""")
                Editmessage(chat_id, text, status)
            elif "Unrecognized request URL" in b:
                text = ("[UPDATE] PROXIES ERROR")
                Editmessage(chat_id, text, status)
            elif response.status_code == 200:
                text = (f"""
✔️CC➟ <code>{cc[:7]}xxxxxxxxxx|{mes}|{ano}|{cvv}</code>
STATUS ➟ #ApprovedCVV 
Response -» Successfully Charged 1$ {dia} 
Gateway -» Stripe Charge 1$ 
VBV[3D] {crs} {vs}
TOOK: {toc - tic:0.4f}s
CHECKED BY @ASURCCWORLDBOT
Used by @{userid}
""")
                Editmessage(chat_id, text, status)
            else:
                if msg ==  "Your card has insufficient funds.":
                    msg = "Your card has insufficient funds ✅"
                    text=(f"""
{wdia} CC {crs} <code>{cc[:7]}xxxxxxxxx|{mes}|{ano}|{cvv}</code> \n STATUS {crs} Declined \n MSG {crs} {msg} \n TOOK: {toc - tic:0.4f} \n CHECKED BY @ASURCCWORLDBOT \n
Used by @{userid}
""")
                else:
                    text=(f"""
{wdia} CC {crs} <code>{cc[:7]}xxxxxxxxx|{mes}|{ano}|{cvv}</code> \n STATUS {crs} Declined \n MSG {crs} {msg} \n TOOK: {toc - tic:0.4f} \n CHECKED BY @ASURCCWORLDBOT \n
Used by @{userid}
""")
                Editmessage(chat_id, text, status)

    except IndexError:
        Editmessage(chat_id, 'Enter Valid CCs Format!!', status)
        return
        

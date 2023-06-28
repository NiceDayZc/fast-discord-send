from tls_client import Session ; session = Session(client_identifier="chrome110",random_tls_extension_order=True)
from itertools import cycle
from threading import Thread
from time import sleep
from os import system
from datetime import datetime
from colorama import Fore
import time

from nicedayLOG.logger import Output

def message_req(tokens, channel_id, message, ThreadCOUNT):
    try:
        poof = time.time()
        message_response = session.post(f"https://discord.com/api/v9/channels/{channel_id}/messages",headers={"accept": "*/*","accept-language": "en-US,th;q=0.9","authorization": tokens,"content-type": "application/json","sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\"","sec-ch-ua-mobile": "?0","sec-ch-ua-platform": "\"Windows\"","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","x-debug-options": "bugReporterEnabled","x-discord-locale": "th","x-discord-timezone": "Asia/Bangkok","x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC43MCIsIm9zX3ZlcnNpb24iOiIxMC4wLjE5MDQ1Iiwib3NfYXJjaCI6Ing2NCIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdPVzY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBkaXNjb3JkLzEuMC43MCBDaHJvbWUvMTA4LjAuNTM1OS4yMTUgRWxlY3Ryb24vMjIuMy4xMiBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMjIuMy4xMiIsImNsaWVudF9idWlsZF9udW1iZXIiOjIwOTM2MSwibmF0aXZlX2J1aWxkX251bWJlciI6MzQyNTcsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"},
        json={"content" : F"{message}","nonce": "","tts": False,"flags": 0})  
        if message_response.status_code in [200, 201, 204]:
            Output("SUCCESS").log(f'[{ThreadCOUNT}] SEND {tokens[:30]} SUCCESS IN {round(time.time()-poof)}s')

        elif message_response.status_code == 429:
            Output("ERROR").log(f'[{ThreadCOUNT}] {tokens[:30]} : RATE LIMITED {message_response.json()["retry_after"]}')
            sleep(message_response.json()['retry_after'])
            return message_req(tokens, channel_id, message, ThreadCOUNT)
    except:pass

if (__name__ == '__main__'):
    time_now = datetime.now().strftime("%H:%M:%S")
    tokens_x = cycle(open('tokens.txt', 'r+').read().splitlines())
    system("cls")
    channel_id      = input(F"[{Fore.LIGHTBLACK_EX}{time_now}{Fore.RESET}] ({Fore.LIGHTBLACK_EX}?{Fore.RESET}) channel id > ")
    message         = input(F"[{Fore.LIGHTBLACK_EX}{time_now}{Fore.RESET}] ({Fore.LIGHTBLACK_EX}?{Fore.RESET}) message > ")
    overloadThread  = int(input(F"[{Fore.LIGHTBLACK_EX}{time_now}{Fore.RESET}] ({Fore.LIGHTBLACK_EX}?{Fore.RESET}) thread recommended [{len(open('tokens.txt').readlines()) * 5}] > "))
    try:
        for ThreadCOUNT in range(overloadThread):
            for you in range(len(open('tokens.txt').readlines())):
                Thread(target=message_req, args=(next(tokens_x), channel_id, message, ThreadCOUNT,)).start()
                Output("INFO").log(f'[{ThreadCOUNT}] HAS START')
        del channel_id           
        del message
        del overloadThread
        del tokens_x
        del ThreadCOUNT

    except:pass

import urllib.request
import json
from gtts import gTTS
from playsound import playsound
import os
import sys
from random import choice
import requests
from lxml import html


class Komut():
    def __init__(self,gelenSes):
        self.ses = gelenSes.upper()
        self.sesBloklari = self.ses.split()
        print(self.sesBloklari)
        self.komutlar = ["ABONE","CEVİR","NASILSIN","KAPAT","HAVA"]
    
    def seslendirme(self,yazi):
        tts = gTTS(text=yazi,lang='tr')
        tts.save("ses.mp3")
        playsound("ses.mp3")
        os.remove("ses.mp3")
        print(yazi)
        
    def nasılsın(self):
        self.seslendirme("iyiyim canım sen nasılsın")    
        
    def kapat(self):
        self.seslendirme("şu an kapatıyorum")
        
    def havadurumu(self):
        self.seslendirme("hava çok güzel")
        
    def komutBul(self):
        for komut in self.komutlar:
            if komut in self.sesBloklari:
                self.komutCalistir(komut)
                
    def komutCalistir(self,komut):
        if komut == "HAVA":
            self.havadurumu()
            
        if komut == "KAPAT":
            self.kapat()
            
        if komut == "NASILSIN":
            self.nasılsın()
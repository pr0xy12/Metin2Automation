#!usr/bin/env python3
#-*- coding:utf-8 -*-
# https://www.github.com/pr0xy12

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from requests import status_codes
from bs4 import BeautifulSoup
from sys import exit
from datetime import datetime
from platform import python_version
from time import sleep
from os import name
from os import system
from colorama import Fore, Back, Style
import colorama
import platform

class AppData(object):
    def Appİnformation(self):
        self._OS_ = "Linux and Windows"
        self._VERSION_ = "V1.0.0"
        self._APPNAME_ = "Metin2_AutomationLogin"
        self._DEV_ = "pr0xy12"

class pColor:
    WARNING = '\033[91m'
    DEFAULT = '\033[0m'
    WHITE = '\033[46m'

class Module_Control(object):
    def CONTROL():
        if int(python_version()[0]) < 3:
            print("{0}[!]{1}{2} Python Version 3 Kullanınız.".format(pColor.WARNING, pColor.DEFAULT, pColor.WHITE))
            exit()

        try:
            import selenium
            from selenium import webdriver
            return True
        except:
            print("{0}[!]{1}{2} Selenium Modülünüz Yüklü Değildir..".format(pColor.WARNING, pColor.DEFAULT, pColor.WHITE))
        
        try:
            import colorama
            from colorama import Fore, Back, Style
            return True
        except:
            print("{0}[!]{1}{2} Colorama Modülünüz Yüklü Değildir..".format(pColor.WARNING, pColor.DEFAULT, pColor.WHITE))
        
        try:
            import requests
            from bs4 import BeautifulSoup
            return True
        except:
            print("{0}[!]{1}{2} Requests ve BeautifulSoup Modülünüz Yüklü Değildir..".format(pColor.WARNING, pColor.DEFAULT, pColor.WHITE))
            exit()
            

class Metin2_AutomationLogin(object):
    def __init__(self, loginlist, passlist, webdriverpath, site):
        colorama.init()
        self.loginlist = loginlist
        self.passlist = passlist
        self.webdriverpath = webdriverpath
        self.site = site

    def Time(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    
    def LoginPassKontrol(self):
        try:
            with open(self.loginlist, "r") as self.ls:
                print("Toplam da : {0}{1}{2}{3} Kullanıcı adı vardır.".format(Fore.GREEN, Style.BRIGHT, len(self.ls), Fore.RESET))
        except FileNotFoundError:
            print("{0}[!]{1} {2}'Loginlist.txt'{3} Dosyası Bulunamadı.".format(Fore.RED, Fore.RESET, Style.BRIGHT, Style.NORMAL))
        try:
            with open(self.passlist, "r") as self.ps:
                print("Toplam da : {0}{1}{2}{3} Şifre vardır.".format(Fore.GREEN, Style.BRIGHT, len(self.ps), Fore.RESET))
        except FileNotFoundError:
            print("{0}[!]{1} {2}'Passlist.txt'{3} Dosyası Bulunamadı.".format(Fore.RED, Fore.RESET, Style.BRIGHT, Style.NORMAL))

    def AppMenu(self):
        print(r"{0}|  \/  ||  ___|_   _|_   _| \ | |/ __  \ {0}{1}{2}| ___ \|  _  |_   _|{1}".format(Fore.RED, Fore.RESET, Fore.GREEN))
        print(r"{0}| .  . || |__   | |   | | |  \| |`' / /' {0}{1}{2}| |_/ /| | | | | |{1}".format(Fore.RED, Fore.RESET, Fore.GREEN))  
        print(r"{0}| |\/| ||  __|  | |   | | | . ` |  / /   {0}{1}{2}| ___ \| | | | | |{1}".format(Fore.RED, Fore.RESET, Fore.GREEN))  
        print(r"{0}| |  | || |___  | |  _| |_| |\  |./ /___ {0}{1}{2}| |_/ /\ \_/ / | |{1}".format(Fore.RED, Fore.RESET, Fore.GREEN))  
        print(r"{0}\_|  |_/\____/  \_/  \___/\_| \_/\_____/ {0}{1}{2}\____/  \___/  \_/{1}".format(Fore.RED, Fore.RESET, Fore.GREEN))
        print("\n{0}    Developer: {1}{2}{3}pr0xy12{1}\n".format(Fore.GREEN, Fore.RESET, Style.BRIGHT, Fore.RED))
        print("{0}[1]{1} {2}Botu Başlat".format(Fore.GREEN, Fore.RESET, Style.BRIGHT))
        print("{0}[2]{1} {2}Login ve Pass List Kontrolü".format(Fore.GREEN, Fore.RESET, Style.BRIGHT))
        print("{0}[3]{1} {2}Exit".format(Fore.GREEN, Fore.RESET, Style.BRIGHT))

if __name__ == "__main__":
    loginlist = "loginlist"
    passlist = "passlist"
    webdriverpath = "geckodriver"
    site = "https://www.m2zed.com/site"
    hours = datetime.now().strftime("%H")
    minutes = datetime.now().strftime("%M")
    if platform.system == "Windows" or platform.system == "windows":
        system("cls")
    else:
        system("clear")
    Module_Control.CONTROL()
    start = Metin2_AutomationLogin(loginlist, passlist, webdriverpath, site)
    start.AppMenu()
    start.LoginPassKontrol()
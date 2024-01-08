import selenium
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from bsi import BSI
import bsi
import keyboard

edge_options = Options()
edge_options.add_experimental_option("debuggerAddress","127.0.0.1:3241")

edge_options.use_chromium = True
s = Service('msedgedriver.exe')
driver = webdriver.Edge(service = s, options = edge_options)
driver.get('https://google.com')
def pilh():
    pil = input('masukan input : ')
    if pil == '1' :
        BSI().pakeai()
    elif pil == '2':
        while True:
            xpat = input("Masukan XPATH : ")
            BSI().pakepath(xpat=xpat)
            if keyboard.is_pressed(";"):
                break
            


while True:
    pilh()


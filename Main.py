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
driver.get('http://elearning.bsi.ac.id/login')

def pilh():
    print("Pilih menu :\n1.AI\n2.XPATH")
    pil = input('masukan input : ')
    if pil == '1' :
        print("Program berjalan tekan '[' untuk berhenti")
        while True:
            BSI().pakeai(driver=driver)
            if keyboard.is_pressed("["):
                print("Program terhenti")
                break
        pilh()
    elif pil == '2':
        print("Program berjalan tekan '[' untuk berhenti")
        while True:
            BSI().pakepath(driver=driver)
            if keyboard.is_pressed("["):
                print("Program terhenti")
                break
        pilh()

pilh()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import keyboard
import time
from bardai import aigoblog
import unittest

#RUN EDGE WITH PORT 3241
options = webdriver.EdgeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument("--log-level=3")
options.add_experimental_option("detach", True)
options.add_argument('--remote-debugging-port=3241')
options.add_argument('--start-maximized')
path = Service('msedgedriver.exe')
driver2 = webdriver.Edge(options=options, service=path)



class BSI:
    def pakeai(self, driver):
        try :
                driver.switch_to.window(driver.window_handles[1])
                self.soal = driver.find_element(By.XPATH, '//*[@id="form-ujian"]/div[1]/p').text + '\n'
                self.a = 'a. ' + driver.find_element(By.XPATH, '//*[@id="form-ujian"]/div[2]/label[1]').text + '\n'
                self.b = 'b. ' + driver.find_element(By.XPATH, '//*[@id="form-ujian"]/div[2]/label[2]').text + '\n'
                self.c = 'c. ' + driver.find_element(By.XPATH, '//*[@id="form-ujian"]/div[2]/label[3]').text + '\n'
                self.d = 'd. ' + driver.find_element(By.XPATH, '//*[@id="form-ujian"]/div[2]/label[4]').text + '\n'
                self.e = 'e. ' + driver.find_element(By.XPATH, '//*[@id="form-ujian"]/div[2]/label[5]').text + '\n'
                self.soalfull = self.soal + self.a + self.b + self.c + self.d + self.e + "Tanpa penjelasan"
                print(self.soalfull)
                
                aigoblog(self.soalfull)
                if "(a)" in str(aigoblog(self.soalfull)):
                    driver.find_element(By.XPATH, '//*[@id="form-ujian"]/div[2]/label[1]').click()
                elif "(b)" in str(aigoblog(self.soalfull)):
                    driver.find_element(By.XPATH, '//*[@id="form-ujian"]/div[2]/label[2]').click()
                elif "(c)" in str(aigoblog(self.soalfull)):
                    driver.find_element(By.XPATH, '//*[@id="form-ujian"]/div[2]/label[3]').click()
                elif "(d)" in str(aigoblog(self.soalfull)):
                    driver.find_element(By.XPATH, '//*[@id="form-ujian"]/div[2]/label[4]').click()
                elif "(e)" in str(aigoblog(self.soalfull)):
                    driver.find_element(By.XPATH, '//*[@id="form-ujian"]/div[2]/label[]').click()
        except NoSuchElementException:
            return False
        except StaleElementReferenceException:
            return False
        except :
            return False
        return True
    
    def pakepath(self, driver):
        try:
            if keyboard.is_pressed(']'):
                with open('ekspat.txt', 'r') as xp:
                    ekspat = xp.readlines()[0][10:]
                driver.switch_to.window(driver.window_handles[1])
                driver.find_element(By.XPATH, str(ekspat)).click()
                print('dafaprstya')

        except NoSuchElementException:
            return False
        except StaleElementReferenceException:
            return False
        except :
            return False
        return True

# BSI().pakepath()
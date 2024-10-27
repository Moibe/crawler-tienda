from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import webdrivers

def check_exists_by_xpath(xpath, driver):
    
    try:
       elemento = driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
            return 'error'
    return elemento

def buscaProductos(url):


    driver = webdrivers.createDriver(navigator='chrome', width=800, height=600, headless=True)
    #driver = webdriver.Chrome()

    driver.get(url)

    lista_productos = []

    for i in range(1, 16):    
        ruta_xpath = f'/html/body/div[2]/div/div[1]/div/div[5]/div/div[2]/section/div[2]/div/div[5]/div/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[{i}]/section/a/article/div/div[9]/div/h3/span'

        try: 
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, ruta_xpath)))
            print(f"El elemento {i} ha cargado")
        except:
            print("El elemento final no cargó en el tiempo establecido")

        resultado = check_exists_by_xpath(ruta_xpath, driver)
        #print(resultado)
        if resultado == 'error':
            texto = 'No existe'
        else: 
            texto = resultado.text
        
        print(texto)
        lista_productos.append(texto)
        time.sleep(1)

    print("Imprimiendo Lista:")
    print(lista_productos)
    driver.quit()

    return lista_productos

#buscaProductos('https://www.tiendasjumbo.co/supermercado/despensa/harinas-y-mezclas-para-preparar')
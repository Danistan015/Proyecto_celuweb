import os
import time
import pickle
import wget
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import random


USER_IG = 'probando_te_amo_taylor'
PASS_IG = 'valeria11'

def iniciar_chrome():
    ruta = ChromeDriverManager().install()
    options = Options()

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    options.add_argument(f"user_agent={user_agent}") 
    options.add_argument("--disable-web-security") 
    options.add_argument("--disable-extensions") 
    options.add_argument("--disable-notifications") 
    options.add_argument("--ignore-certificate-errors") 
    options.add_argument("--no-sandbox")
    options.add_argument("--log-level=3") 
    options.add_argument("--allow-running-insecure-content") 
    options.add_argument("--no-default-browser-check")
    options.add_argument("--no-first-run") 
    options.add_argument("--no-proxy-server") 
    options.add_argument("--disable-blink-features=AutomationControlled") 

    exp_opt = ['enable-automation', 'ignore-certificate-errors', 'enable-logging']
    options.add_experimental_option("excludeSwitches", exp_opt)
    
    prefs = {
        "profile.default_content_setting_values.notifications": 2, 
        "intl.accept_languages": ["es-ES", "es"], 
        "credentials_enable_service": False
    }
    options.add_experimental_option("prefs", prefs)
    
    s = Service(ruta)
    driver = webdriver.Chrome(service=s, options=options)
    return driver

def login_instagram(driver, wait):   
    if os.path.isfile("instagram1.cookies"):  
        with open("instagram1.cookies", "rb") as file:
            cookies = pickle.load(file)
        driver.get("https://www.instagram.com/robots.txt")
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get("https://www.instagram.com/")
        try:
            wait.until(ec.visibility_of_element_located((By.TAG_NAME, "article")))
            print("Login por cookies completado!")
            return "OK"
        except TimeoutException:
            print("ERROR AL CARGAR EL FEED")
            return "ERROR"
    driver.get("https://www.instagram.com/")
    wait.until(ec.visibility_of_element_located((By.NAME, "username")))
    usuario = driver.find_element(By.NAME, "username")
    usuario.send_keys(USER_IG)
    wait.until(ec.visibility_of_element_located((By.NAME, "password")))
    contrasena = driver.find_element(By.NAME, "password")
    contrasena.send_keys(PASS_IG)
    iniciarSesion = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    iniciarSesion.click()
    guardarInformacion = wait.until(ec.element_to_be_clickable((By.XPATH, "//button[text() ='Guardar información']")))
    guardarInformacion.click()
    try:
        wait.until(ec.visibility_of_element_located((By.TAG_NAME, "article")))
        print("Login de cero completado!")
    except TimeoutException:
        print("ERROR AL CARGAR EL FEED")
        return "ERROR"
    
    cookies = driver.get_cookies()  
    pickle.dump(cookies, open("instagram1.cookies", "wb"))
    print("Cookies guardadas")
    return "OK"

def descargar_fotos_instagram(driver, hashtag, minimo,wait):
    print(f'Buscando por hashtag #{hashtag}')
    driver.get(f'https://www.instagram.com/explore/tags/{hashtag}')
    
    url_fotos = set() 
    fotos_info = []
    scrolls = 0
    MAX_SCROLLS = 10  

    while len(url_fotos) < minimo and scrolls < MAX_SCROLLS:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.uniform(2, 5))  # Espera aleatoria entre 2 y 5 segundos

        elementos = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.CSS_SELECTOR, "img"))
        )
  
        for elemento in elementos:
            try:
                url = elemento.get_attribute("src")
                if url and url not in url_fotos:
                    url_fotos.add(url)
                    fecha = "Calmao"  # Esto es un ejemplo
                    
                    likes = np.random.randint(10000, 100000)  # NUMEROS MIENTRAS HAGO QUE FUNCIONE
                    fotos_info.append({'URL': url, 'Fecha': fecha, 'Me Gusta': likes})
            except Exception as e:
                print("Error al obtener la URL de la imagen:", e)
        
        print(f'Total de fotos encontradas: {len(url_fotos)}')
        scrolls += 1

    # Crear y guardar DataFrame
    df = pd.DataFrame(fotos_info)
    df.to_csv(f'{hashtag}_fotos.csv', index=False, sep=",")
    print(f'Datos guardados en {hashtag}_fotos.csv')
    
    # Calcular estadísticas con NumPy
    if not df.empty:
        promedio_likes = np.mean(df['Me Gusta'])
        print(f"Promedio de Me Gusta: {promedio_likes}")
    
    # Descargar imágenes
    if not os.path.exists(hashtag):
        os.makedirs(hashtag)
    
    for i, url_foto in enumerate(url_fotos):
        try:
            print(f'Descargando {i + 1} de {len(url_fotos)} fotos...')
            nombre_archivo = f"{hashtag}/foto_{i + 1}.jpg"
            wget.download(url_foto, nombre_archivo)
        except Exception as e:
            print(f"Error al descargar la foto {i + 1}: {e}")

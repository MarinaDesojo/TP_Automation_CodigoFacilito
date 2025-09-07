from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def create_driver(headless=False): #headless significa q no tiene interfaz, booleano
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito'),  # con esto abre una ventana de incognito

    if headless:
        options.add_argument("--headless=new")

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), #esto es para que en caso de que no tenga el chrome driver en mi pc la biblioteca lo instale por mi
        options=options,
    )

#    if options is None: #incorporacion de chatgpt: Puedes decidir si prefieres recibirlo por parámetro o definirlo dentro. Por ejemplo:
#        options = webdriver.ChromeOptions()

    driver.implicitly_wait(5)
    return driver



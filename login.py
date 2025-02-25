from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pyautogui
import time
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

load_dotenv()
login_unipar = os.getenv("LOGIN_UNIPAR")
senha_unipar = os.getenv("SENHA_UNIPAR")

email = os.getenv("LOGIN_EMAIL")
senha = os.getenv("SENHA_EMAIL")

url = 'https://lyaluno.unipar.br/aluno/#/login'
options = Options()
options.add_experimental_option("detach", True)
service = Service()
diretorio = r"c:\Users\tiago\Downloads"

prefs = {
    "dowload.default_directory": diretorio,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True

}

options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options= options, service= service)
driver.maximize_window()

driver.get(url)

def inserir_dados(driver):

    login_= driver.find_element(By.XPATH, '/html/body/ion-nav-view/div/div/div[2]/div/form/div/label[1]')
    login_.send_keys(login_unipar)

    senha_ = driver.find_element(By.XPATH, '//*[@id="password"]')
    senha_.send_keys(senha_unipar)

    entrar_ = driver.find_element(By.XPATH, '//*[@id="button-login"]')
    entrar_.click()

def pegar_historico():

    time.sleep(8)
    pyautogui.click(x=109, y=374)

    time.sleep(5)
    pyautogui.click(x=146, y=458)

    time.sleep(2)
    pyautogui.click(x=1017, y=710)

def verificar_dowload(pasta, timeout = 30):
    end_time = time.time() + timeout
    while time.time() < end_time: 
        for filename in os.listdir(pasta):
            if filename.__contains__("60301107"):
                return os.path.join(pasta, filename)
        time.sleep(1)
    return None


def enviar_email():

   

    #configuração email
    ms = MIMEMultipart()
    ms ['From'] = email
    ms ['To'] = email
    ms ['Subeject'] = "assunto"

    arquivo_baixado = verificar_dowload(diretorio, timeout=30)
    if arquivo_baixado:
        part = MIMEBase('application', 'octet-stream')
        encoders.encode_base64(part)
        part.set_payload(open(diretorio, 'rb').read())
        part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(diretorio)}')
        ms.attach(part)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, senha)
        server.sendmail(email, email, ms.as_string())
        server.quit()
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")###


 

inserir_dados(driver)
pegar_historico()
enviar_email()
 #ENTENDER ISSO

# def verificar_download(pasta, timeout=30):

#    end_time = time.time() + timeout

#    while time.time() < end_time:

#        for filename in os.listdir(pasta):

#            if filename.endswith(".pdf"):  # Substitua pela extensão do arquivo baixado

#                return os.path.join(pasta, filename)

#        time.sleep(1)

#    return None
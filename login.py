from selenium import webdriver  
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service



url = 'https://lyaluno.unipar.br/aluno/#/login'

options = Options()
options.add_experimental_option("detach", True)
service = Service()
driver = webdriver.Chrome(options= options, service= service)


driver.get(url)
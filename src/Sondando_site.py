from selenium import webdriver 
from selenium.webdriver.common.by import By  


class WebScraping:
    def __init__(self):
        self.driver = webdriver.Chrome()

    #função que acessa ao sites
    def sondando_site(self):
        self.driver = webdriver.Chrome()
        url = 'https://br-vapers.com/collections/kit-iniciante-starter-kits'
        self.driver.get(url)


    #função que pega todos os nomes do produtos de eu site e coloca em uma lista
    def extraindo_produtos_web(self):    
        self.sondando_site()
        class_produto = self.driver.find_elements_by_class_name('product-card__name')
        nome_produto = []
        
        for produto in class_produto:
            nome_produto.append(produto.text)
        
        return nome_produto
        

    #função que pega todos os preços do produtos de eu site e coloca em uma lista
    def extraindo_preco_web(self):
        self.sondando_site()
        class_preco = self.driver.find_elements_by_class_name('product-card__price')
        preco_produto = []

        for preco in class_preco:
            preco_produto.append(preco.text)

        return preco_produto     




    

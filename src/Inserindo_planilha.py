from openpyxl import Workbook
from Sondando_site import WebScraping

#class que vai pegar os dados do site e inserir nas planilhas
class Enviando_para_panilha:
    
    def __init__(self):
        self.wb = Workbook()
        self.websc = WebScraping() 

    def criar_planilhas(self):
        #pegou a primeira pagina da planilha
        planilha = self.wb.worksheets[0]
        

        planilha['A1'] = 'Produto'
        planilha['B1'] = 'Preço'
         

        nome_produtos = self.websc.extraindo_produtos_web()
        preco_produtos = self.websc.extraindo_preco_web()
        
        #problema e que esta retornando em apenas colunas diferentes
        quantidade_linhas = len(nome_produtos)
        
        for linha in range(2,quantidade_linhas): 
            planilha['B'+str(linha)] = preco_produtos[linha]
            planilha['A'+str(linha)] = nome_produtos[linha]
            
        self.wb.save('.\consulta_de_preço.xlsx')
            
        

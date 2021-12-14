from os import error
import smtplib
import email
from email.message import EmailMessage
from email.mime.base import MIMEBase
import email.mime.application

class Envioemail:
    
    def __init__(self):
        self.msg = EmailMessage()

    def criar_e_enviar_email(self):
        #insira o email e a senha
        email_usuario = input('Digite seu email: ')
        senha = str(input('Digite sua senha: '))

        #criar email
        self.msg['Subject'] = 'Planilhas com relação de produto e preço'
        self.msg['From'] = email_usuario
        self.msg['To'] = input('digite o email para quem você deseja enviar: ')

        #abrimos o arquivo em modo de leitura binaria
        filename = '.\consulta_de_preço.xlsx'
        fp = open(filename,'rb')

        #lemos o arquivo no modo binario e jogamos ele para xlsx
        att = email.mime.application.MIMEApplication(fp.read(),_subtype="xlsx")
        att.add_header('Content-Disposition','attachment',filename=filename)
        self.msg.add_attachment(att)

        #fazendo login e enviando email com os parametros acima
        with smtplib.SMTP_SSL(host='smtp.gmail.com',port= 465) as smtp:
                   
            try:
                smtp.login(email_usuario,senha)
                smtp.send_message(self.msg)
                smtp.quit() 
                print('email enviado com sucesso!!')
            
            except error(OSError):
                print('você digitou alguns dos dados errados')
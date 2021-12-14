from Inserindo_planilha import Enviando_para_panilha
from enviar_email import Envioemail

def main ():
    iniciando_planiha = Enviando_para_panilha()
    iniciando_planiha.criar_planilhas()

    enviado_planilha_email = Envioemail()
    enviado_planilha_email.criar_e_enviar_email()

main()
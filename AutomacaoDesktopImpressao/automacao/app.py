import pyautogui as pg
import logging as log

from automacao.exceptions import ErroAutomacao
from automacao.utils import Utils
from automacao.settings import Settings
from automacao.service import Service

class Automacao:
    def __init__(self):
        utils = Utils()
        settings = Settings()
        
        self.service = Service(utils, settings)

    def executar(self):
        try:
            pg.alert("Automação iniciada")

            self.service.abrir_programa()
            self.service.configurar_impressao()
            self.service.imprimir_cartoes()
            
            pg.alert("Automação finalizada com sucesso")

        except ErroAutomacao as e:
            self.service.salvar_screenshot(contexto = str(e))

            log.error(f"Falha lógica: {e}")
            pg.alert(text = str(e), title = "Erro na Automação")

        except Exception as e:
            log.critical(f"Erro inesperado: {e}")
            pg.alert(f"Erro inesperado: {e}")
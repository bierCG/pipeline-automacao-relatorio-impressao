import time
import logging
import pyautogui as pg
import pygetwindow as gw
from pathlib import Path
from datetime import datetime

from automacao.settings import Settings

class Utils:
    def __init__(self):
        self.settings = Settings()
        pg.PAUSE = self.settings.PG_PAUSE 

    @staticmethod
    def get_center(x, y, largura, altura):
        return x + (largura / 2), y + (altura / 2)

    def click(self, x: int, y: int, clicks: int = 1) -> None:
        pg.click(x, y, clicks = clicks)

    def open_folder(self, path: str):
        pg.hotkey('win', 'r')
        pg.write(path)
        pg.press('enter')

    def locate_image(self, imagem: str):
        logging.info(f'Procurando imagem: {imagem}')

        tempo_espera = time.time() + self.settings.TIMEOUT_BUSCA
        caminho = Path(self.settings.PATH_PASTA_ASSETS) / imagem

        while time.time() < tempo_espera:
            if localization := self.locate_on_screen(caminho):
                return localization
            
            time.sleep(self.settings.INTERVALO_BUSCA)
        return None
    
    def screenshot(self, contexto: str) -> None:
        try:
            diretorio = Path('assets') / 'screenshot_errors'
            diretorio.mkdir(parents = True, exist_ok = True)

            nome_arquivo = f'{contexto}_{datetime.now():%Y%m%d_%H%M%S}.png'
            caminho_arquivo = diretorio / nome_arquivo

            pg.screenshot(str(caminho_arquivo))

            logging.warning(f'Screenshot do erro salvo: {nome_arquivo}')
        except Exception as e:
            logging.exception(f'Erro ao capturar screenshot: {e}')

    def maximaze_window(self):
        try:
            window = gw.getActiveWindow()
            if window and not window.isMaximized:
                window.maximize()
        except Exception as e:
            logging.warning(f'Erro ao maximizar janela: {e}')

    def locate_on_screen(self, caminho: Path):
        try:
            return pg.locateOnScreen(
                str(caminho),
                grayscale = self.settings.PG_GRAYSCALE,
                confidence = self.settings.PG_CONFIDENCE
            )
        except Exception as e:
            logging.exception(f'Erro ao localizar imagem: {e}')
            return None
        
    def get_cards_number(self):
        try:
            with open(
                self.settings.PATH_ARQUIVO_INTEGRACAO,
                'r',
                encoding = self.settings.ENCODING_FILE
            ) as file:
                return len(file.readlines())
        except Exception:
            logging.exception('Erro ao pegar número de cartões')
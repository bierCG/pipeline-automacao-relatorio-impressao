from automacao.exceptions import ErroAutomacao

import time
import logging

class Service:
    def __init__(self, utils, settings):
        self.utils = utils
        self.settings = settings
        
        self.botoes = {
            '': ()
        }
 
        self.fluxos = {
            '': []
        }

    def _wait(self, tempo: float):
        time.sleep(tempo)

    def _clicar_imagem(self, img: str, cliques: int = 1) -> None:
        local = self.utils.locate_image(img)
        if not local:
            logging.error(f'Arquivo não encontrado: {img}')
            raise ErroAutomacao(f'Imagem não encontrada: {img}')
        
        coordenadas = self.utils.get_center(*local)
        self.utils.click(*coordenadas, clicks = cliques)

    def abrir_programa(self) -> None:
        logging.info("Abrindo programa de impressão")

        self.utils.open_folder(self.settings.PATH_PASTA_PROGRAMA_IMPRESSAO)
        self.utils.maximaze_window()

        self._clicar_imagem('arquivo_programa_impressao.png', cliques = 2)

        if not self.utils.locate_image('importar_arquivo_integracao.png'):
            logging.warning('Erro ao tentar abrir o programa de impressão')
            raise ErroAutomacao('Erro ao tentar abrir o programa de impressão')
        
    def configurar_impressao(self) -> None:
        logging.info('Configurando formato de impressão')

        self._clicar_imagem('importar_arquivo_integracao.png')

        for imagem in self.fluxos['configurar_formato_impressao']:
            self._clicar_imagem(imagem, clicks = 1)

    def imprimir_cartao(self) -> None:
        self.utils.click(*self.botoes['IMPRIMIR'])
        self._wait(2)
        
        self.utils.click(*self.botoes['CONFIRMAR'])
        self._wait(2)

    def imprimir_cartoes(self) -> None:
        logging.info('Imprimindo cartões')

        numero_cartoes = self.utils.get_cards_number()

        while numero_cartoes > 0:
            lote = min(numero_cartoes, 10)

            for _ in range(lote):
                self.imprimir_cartao()

            numero_cartoes -= lote

    def salvar_screenshot(self, contexto: str) -> None:
        self.utils.screenshot(contexto)
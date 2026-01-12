from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    InvalidArgumentException
)

from datetime import datetime
from pathlib import Path
import logging
import os

class Script():
    def __init__(self):
        self.SITE = os.getenv('SITE')
        self.USER = os.getenv('USUARIO')
        self.PASSWORD = os.getenv('SENHA')
        self.CLIENTE = os.getenv('CLIENTE')

        self.PASTA_ARQUIVO = os.getenv('PASTA_ARQUIVO')
        self.NOME_NOVO_ARQUIVO = os.getenv('NOME_NOVO_ARQUIVO')

        self.ID_INPUT_USUARIO = os.getenv('ID_INPUT_USUARIO')
        self.ID_INPUT_SENHA = os.getenv('ID_INPUT_SENHA')
        self.ID_BOTAO_LOGIN = os.getenv('ID_BOTAO_LOGIN')
        self.ID_BOTAO_RELATORIO = os.getenv('ID_BOTAO_RELATORIO')
        self.ID_DROPDOWN_CLIENTES = os.getenv('ID_DROPDOWN_CLIENTES')
        self.ID_BOTAO_CONFIRMAR = os.getenv('ID_BOTAO_CONFIRMAR')
        self.TAG_FONTE_DADOS = os.getenv('TAG_FONTE_DADOS')

        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')

        self.TEMPO_ESPERA = float(os.getenv('TEMPO_ESPERA_DRIVER', 10))
        self.driver = webdriver.Chrome(options = options)
        self.wait = WebDriverWait(self.driver, float(self.TEMPO_ESPERA))

    def _salvar_screenshot(self, prefixo = 'erro'):
        pasta = Path('assets') / 'screenshot_errors'
        pasta.mkdir(exist_ok = True)

        caminho = pasta / f'{prefixo}_{datetime.now():%d-%m-%Y_%H.%M}.png'
        self.driver.save_screenshot(str(caminho))
        logging.info(f'Screenshot salvo: {caminho}')

    def _carregar_site(self):
        self.driver.get(self.SITE)
        logging.info('Site aberto')

    def _coletar_dados(self):
        # --- Executar o login ---
        self.wait.until(EC.visibility_of_element_located((By.ID, self.ID_INPUT_USUARIO))).send_keys(self.USER)
        self.wait.until(EC.visibility_of_element_located((By.ID, self.ID_INPUT_SENHA))).send_keys(self.PASSWORD)
        self.wait.until(EC.element_to_be_clickable((By.ID, self.ID_BOTAO_LOGIN))).click()

        logging.info('Login executado')

        # --- Gerar o relatório ---
        self.wait.until(EC.element_to_be_clickable((By.ID, self.ID_BOTAO_RELATORIO))).click()

        select = Select(self.driver.find_element(By.ID, self.ID_DROPDOWN_CLIENTES))
        select.select_by_visible_text(self.CLIENTE)

        self.wait.until(EC.element_to_be_clickable((By.ID, self.ID_BOTAO_CONFIRMAR))).click()

        # Espera nova aba com os dados abrir
        self.wait.until(EC.number_of_windows_to_be(2))

        abas = self.driver.window_handles
        self.driver.switch_to.window(abas[1])

        dados = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, self.TAG_FONTE_DADOS))).text

        logging.info('Relatório extraído')

        return dados

    def _criar_arquivo(self, dados):
        pasta = Path(self.PASTA_ARQUIVO)
        pasta.mkdir(parents = True, exist_ok = True)

        nome = f'{self.NOME_NOVO_ARQUIVO} {datetime.now():%d-%m-%Y %H.%M}.txt'
        arquivo = pasta / nome
        arquivo.write_text(dados, encoding = 'utf-8')

        logging.info(f'Arquivo criado: {arquivo}')

    def executar(self):
        try:
            logging.info('Automacao iniciada')

            self._carregar_site()
            dados = self._coletar_dados()

            if not dados.strip():
                raise ValueError('Dados coletados estão vazios')

            self._criar_arquivo(dados)

            logging.info('Automacao finalizada')

        except TimeoutException as e:
            self._salvar_screenshot()
            logging.error('Timeout ao aguardar elemento ou ação do navegador')
            logging.debug(e)

        except NoSuchElementException as e:
            self._salvar_screenshot()
            logging.error('Elemento não encontrado na página')
            logging.debug(e)

        except InvalidArgumentException as e:
            logging.error('Argumento inválido passado ao Selenium')
            logging.debug(e)

        except ValueError as e:
            logging.warning(f'Validação falhou: {e}')

        except Exception as e:
            logging.exception('Erro inesperado na automação')

        finally:
            self.driver.quit()
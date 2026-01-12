from automacao.app import Automacao
import logging

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - [%(levelname)s] - %(message)s",
    handlers = [logging.FileHandler('logs/automacao.log'), logging.StreamHandler()]
)

if __name__ == '__main__':
    Automacao().executar()
from automacao.script import Script
from dotenv import load_dotenv
import logging

load_dotenv()

logging.basicConfig(
    filename = r'',
    level = logging.INFO,
    format = '%(asctime)s | %(levelname)s | %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S'
)

if __name__ == '__main__':
    Script().executar()
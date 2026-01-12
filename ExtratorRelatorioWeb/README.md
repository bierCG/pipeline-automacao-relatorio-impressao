# Automação de Extração de Relatório Web (Selenium)

Projeto de automação desenvolvido em Python para acessar um sistema web, realizar login, gerar um relatório e salvar os dados extraídos em um arquivo `.txt`.

A automação utiliza Selenium para interação com o navegador e segue boas práticas como uso de variáveis de ambiente, logging e tratamento de exceções.

---

## Funcionalidades

- Acesso automático a sistema web
- Login com credenciais via `.env`
- Geração de relatório por cliente
- Extração de dados em nova aba
- Salvamento dos dados em arquivo `.txt`
- Registro de logs da execução
- Captura de screenshot em caso de erro

---

## Tecnologias utilizadas

- Python 3.11.2
- Selenium
- python-dotenv
- Google Chrome / ChromeDriver 120.x

---

## Estrutura do projeto

.
├── main.py
├── script.py
├── automacao.log
├── .env.example
├── screenshots/

---

## Observações
- O projeto depende de elementos específicos da página (IDs e tags).
- Alterações no layout do site podem exigir ajustes nos seletores.
- Recomendado utilizar ChromeDriver compatível com a versão do Google Chrome instalada.

📌 Objetivo do projeto
Projeto criado para fins de estudo e portfólio, demonstrando automação web com Python, Selenium e boas práticas de organização de código.
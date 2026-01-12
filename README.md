# Pipeline de Automação de Relatórios e Impressão de Cartões

## Visão Geral

Este repositório faz parte de um **pipeline completo de automação**, composto por dois projetos complementares:

1. **Extração de Relatórios (Web Automation)**
   Automação via Selenium responsável por acessar um sistema web, aplicar filtros, validar dados e gerar um arquivo de relatório (TXT/CSV) com as informações dos cartões.

2. **Automação Desktop de Impressão (este projeto)**
   Automação desktop desenvolvida em Python com PyAutoGUI que consome o relatório gerado, interage com uma aplicação desktop de impressão e executa todo o fluxo operacional de forma automatizada.

O objetivo do pipeline é simular um **fluxo real de produção**, demonstrando capacidade de análise, automação de processos, organização de código e boas práticas de engenharia de software.

---

## Arquitetura do Pipeline

```text
[Sistema Web]
      |
      | (Selenium)
      v
[Extração de Relatório]
      |
      | Arquivo TXT/CSV
      v
[Automação Desktop]
      |
      | (PyAutoGUI)
      v
[Aplicação de Impressão]
```

Cada etapa é desacoplada, permitindo manutenção, testes e evolução independentes.

---

## Tecnologias Utilizadas

### Extração de Relatórios

* Python 3.11+
* Selenium
* WebDriver Manager / ChromeDriver
* python-dotenv
* Logging

### Automação Desktop

* Python 3.11+
* PyAutoGUI
* Pillow
* Logging
* python-dotenv

---

## Estrutura do Projeto (Automação Desktop)

```text
automacao_desktop_pyautogui/
│
├── automacao/
│   ├── app.py           # Orquestração da automação
│   ├── service.py       # Regras de negócio e fluxo principal
│   ├── utils.py         # Funções utilitárias (imagens, delays, validações)
│   ├── settings.py      # Configurações centralizadas
│   └── exceptions.py    # Exceções customizadas
│
├── assets/              # Imagens utilizadas para reconhecimento de tela
│   └── screenshot_errors/# Evidências de falhas
│
├── logs/
│   └── automacao.log    # Log de execução
│
├── .env.example         # Variáveis de ambiente
├── main.py              # Entry point
└── README.md
```

---

## Funcionalidades

* Consumo automático de relatório gerado via web
* Abertura e navegação em aplicação desktop
* Importação de arquivos de dados
* Configuração de parâmetros de impressão
* Tratamento de erros com screenshots automáticos
* Logging detalhado para auditoria e debugging
* Uso de exceções customizadas para controle de fluxo

---

## Boas Práticas Aplicadas

* Separação de responsabilidades (Service, Utils, Settings)
* Código modular e reutilizável
* Variáveis sensíveis isoladas em `.env`
* Logs estruturados com timestamps
* Evidências visuais de erro (screenshots)
* Tratamento explícito de falhas operacionais

---

## Como Executar

### Pré-requisitos

* Python 3.11+
* Sistema operacional Windows
* Aplicação desktop alvo instalada

### Instalação

```bash
pip install -r requirements.txt
```

### Configuração

1. Copie o arquivo `.env.example` para `.env`
2. Ajuste os caminhos, tempos e parâmetros conforme o ambiente

### Execução

```bash
python main.py
```

---

## Contexto Profissional

Este projeto foi desenvolvido com foco em **automação corporativa**, simulando cenários reais de produção, onde sistemas web e aplicações desktop coexistem.

Ele demonstra competências essenciais para um **Desenvolvedor Backend Python Júnior com foco em Automação/RPA**, incluindo:

* Leitura e transformação de dados
* Integração entre sistemas
* Automação de processos manuais
* Código limpo e estruturado
* Visão de pipeline e não apenas scripts isolados

---

## Próximos Passos (Evolução Natural)

* Substituir PyAutoGUI por API ou integração nativa (quando disponível)
* Criar camada de testes automatizados
* Containerização do pipeline
* Orquestração via scheduler (Airflow, cron, etc.)

---

## Autor

Gabriel Schlumberger

Desenvolvedor Python | Automação | Backend

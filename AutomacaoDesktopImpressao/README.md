# Automação Desktop de Impressão com PyAutoGUI

## Visão Geral

Este projeto é uma **automação desktop em Python** desenvolvida para simular e automatizar um processo operacional real: **importação e impressão de cartões a partir de um arquivo de relatório**.

A automação **consome um relatório previamente gerado por outro sistema** (extração web), interage com uma aplicação desktop legada e executa todo o fluxo de forma automática, reduzindo erros manuais e tempo operacional.

Este repositório representa a **segunda etapa de um pipeline de automação**, focado em cenários onde **não existe API ou integração nativa disponível**.

---

## Contexto do Problema

Em ambientes corporativos, é comum a existência de sistemas legados que:

* Não possuem API
* Exigem interação manual via interface gráfica
* Dependem de importação de arquivos para execução de tarefas críticas

Este projeto resolve esse cenário automatizando a interação com a aplicação desktop, mantendo controle, logs e evidências de execução.

---

## Tecnologias Utilizadas

* Python 3.11+
* PyAutoGUI
* Pillow
* python-dotenv
* Logging

---

## Arquitetura da Automação

```text
[Arquivo de Relatório]
        |
        v
[Leitura e Validação]
        |
        v
[Automação Desktop]
        |
        v
[Aplicação de Impressão]
```

A automação é estruturada de forma modular, permitindo manutenção, ajustes de timing e reutilização de componentes.

---

## Estrutura do Projeto

```text
automacao_desktop_pyautogui/
│
├── automacao/
│   ├── app.py           # Inicialização e controle da automação
│   ├── service.py       # Fluxo principal e regras de negócio
│   ├── utils.py         # Funções utilitárias (delays, imagens, validações)
│   ├── settings.py      # Configurações centralizadas
│   └── exceptions.py    # Exceções customizadas
│
├── assets/
│   ├── images/          # Imagens para reconhecimento de tela
│   └── screenshot_errors/# Evidências de falha
│
├── logs/
│   └── automacao.log    # Logs detalhados de execução
│
├── .env.example         # Variáveis de ambiente
├── main.py              # Entry point da aplicação
└── README.md
```

---

## Funcionalidades

* Consumo de arquivo de relatório (TXT/CSV)
* Abertura automática da aplicação desktop
* Navegação por menus e telas
* Importação de arquivos de dados
* Configuração de parâmetros de impressão
* Execução do processo de impressão
* Captura automática de screenshots em caso de erro
* Logging estruturado para auditoria e debugging

---

## Boas Práticas Aplicadas

* Separação clara de responsabilidades
* Código modular e reutilizável
* Uso de exceções customizadas
* Variáveis sensíveis isoladas em `.env`
* Logs com timestamps e níveis de severidade
* Evidências visuais para análise de falhas

---

## Limitações Conhecidas

* Dependência de resolução de tela e layout da aplicação
* Sensível a mudanças visuais do sistema automatizado

Essas limitações são conhecidas e assumidas, pois refletem a realidade de automações em sistemas legados sem API.

---

## Como Executar

### Pré-requisitos

* Python 3.11.2
* Sistema operacional Windows
* Aplicação desktop alvo instalada
* Resolução de tela compatível com os assets

## Contexto Profissional

Este projeto foi desenvolvido com foco em **automação corporativa e RPA**, simulando um fluxo real de produção encontrado em ambientes empresariais.

Demonstra:

* Integração entre sistemas
* Automação de processos manuais
* Estruturação de código
* Tratamento de falhas operacionais

---

## Possíveis Evoluções

* Substituir automação de tela por integração via API (quando disponível)
* Implementar testes automatizados
* Criar camada de orquestração (scheduler)
* Monitoramento centralizado

---

## Autor

Gabriel Schlumberger

Desenvolvedor Python | Automação | Backend

# Comparador de Preços – Xbox Series S 🎮


Este projeto faz scraping das lojas **Mercado Livre** e **Casas Bahia** para descobrir o **menor preço disponível** do Xbox Series S, utilizando **Selenium** para lidar com sites que carregam conteúdo via JavaScript.

## 🎯 Objetivo
Automatizar a busca de preços do Xbox Series S e retornar:

- Preço encontrado em cada loja  
- Nome do produto  
- Menor preço entre elas

## 💻 Tecnologias

- Python 3.10+  
- Selenium  
- Chrome ou Firefox com driver correspondente

## 📝 Requisitos Técnicos

Antes de rodar o projeto, você precisará:

**1. Instalar dependências:**

```bash
pip install selenium
```
**2. Baixar o driver do navegador:**
 
- Chrome: [ChromeDriver](https://sites.google.com/chromium.org/driver/)

- Firefox: [GeckoDriver](https://github.com/mozilla/geckodriver/releases)

**3. Colocar o driver em uma pasta do PATH do seu sistema, ou informar o caminho no script.**

**🚀 Como executar:**

Na pasta principal do projeto:
```bash
cd src
python main_selenium.py
```
O script irá abrir o navegador em modo headless, buscar os preços e exibir os resultados no terminal.

**🔍 Como funciona:**

O script realiza os seguintes passos:

**1** - Abre o navegador via Selenium

**2** - Acessa cada loja

**3** - Aguarda o carregamento do conteúdo via JavaScript

**4** - Extrai preço e nome do produto

**5** - Compara os preços e exibe o menor

**⚠️ Avisos**

Selenium é mais pesado que Requests + BeautifulSoup

O script depende da estrutura do site; mudanças podem quebrar a busca

Sites podem bloquear bots se houver muitas requisições

**📁 Estrutura do projeto:**
```bash
preco-xbox/
│── src/
│   ├── main_selenium.py
│   ├── mercado_livre_selenium.py
│   └── casas_bahia_selenium.py
│
├── requirements.txt
├── README.md
└── .gitignore
```
**📄 Licença**

Este projeto está sob a licença MIT:

Copyright (c) 2025 Ana Carolina

## ✏️ Autor

Desenvolvido por [Ana Carolina Jerônimo](https://github.com/anacjeronimo) 🦇


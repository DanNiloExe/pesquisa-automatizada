# 🔍 Pesquisa Automatizada com IA

[![GitHub license](https://img.shields.io/github/license/DanNiloExe/pesquisa-automatizada?style=flat-square&color=blue)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue?style=flat-square&logo=python)](https://www.python.org/)

Este repositório contém uma solução automatizada em Python voltada para a criação, estruturação e engenharia de conteúdo de alto impacto para canais digitais e redes sociais. Utilizando o SDK oficial do Google Generative AI (`google-generativeai`), o ecossistema consome modelos de IA para automatizar postagens estratégicas no LinkedIn e roteiros dinâmicos com técnicas avançadas de retenção para o YouTube.

---

## 📌 Índice
- [Funcionalidades](#-funcionalidades)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Configuração e Instalação](#-configuração-e-instalação)
- [Como Executar](#-como-executar)
- [Exemplos de Saída (Outputs)](#-exemplos-de-saída-outputs)
- [Contribuição](#-contribuição)
- [Licença](#-licença)

---

## ⚡ Funcionalidades

### 1. Gerador de Posts para LinkedIn (`Gerador-de-pesquisas-Gemini.py`)
* **Persona de Especialista:** Atua sob o papel de um analista em *Branding Pessoal* e posicionamento de marca.
* **Refinamento de Tom:** Constrói uma escrita com autoridade corporativa, mas quebra o padrão rígido utilizando leveza, bom humor e parágrafos escaneáveis.
* **Estrutura de Alta Performance:** Focado em ganchos iniciais fortes, 3 dicas práticas de aplicação imediata, provocações sobre burocracias e um CTA direcionado ao engajamento (com uso controlado de até 3 emojis e 3 hashtags).
* **Armazenamento em Histórico:** Salva os posts em lote no arquivo local `dados-pesquisa.json` sem sobrescrever dados anteriores.

### 2. Gerador de Roteiros para YouTube (`Gerador-de-roteiros.py`)
* **Engenharia de Retenção:** Desenvolve roteiros profissionais divididos em blocos estratégicos: *Hook* (gancho magnético de 15-30s), Introdução (proposta de valor), Corpo do Roteiro fragmentado em cenas detalhadas e Gatilhos de Retenção (*Open Loop*).
* **Direção de Arte & Produção:** O prompt instrui a IA a gerar sugestões exatas de falas do apresentador combinadas com indicações de **B-Roll** (cortes de vídeo, inserções de gráficos, tabelas e transições visuais).
* **Estratégia de Conversão (CTA):** Chamadas de ação orgânicas integradas à narrativa.
* **Metadados (Clickgap):** Sugere 3 opções de títulos altamente clicáveis e esboça o conceito visual completo para o design da miniatura (Thumbnail).

---

## 🛠️ Tecnologias Utilizadas

* **[Python](https://www.python.org/):** Linguagem back-end para controle de fluxos, E/S de arquivos e automação.
* **[Google Generative AI SDK](https://pypi.org/project/google-generativeai/):** Integração nativa para chamada e consumo de modelos generativos da API do Gemini.
* **[DateTime](https://docs.python.org/3/library/datetime.html):** Controle de temporização para gerar registros históricos e logs de arquivos dinâmicos.

---

### 🛠️ Configuração e Uso

Instalar a biblioteca para poder utilizar o gemini, diretamente no terminal<br>
pip install -U -q google-generativeai

1. Obtenha sua API Key do Gemini<br>
Para que o script funcione, você precisa de uma chave de acesso oficial da Google:

Acesse o Google AI Studio.<br>
Faça login com sua conta Google.<br>
Clique em "Create API key".<br>
Copie a chave gerada.

No código Python, substitua o valor da de onde está sinalizada a GOOGLE_API_KEY pela sua chave:

##Python
GOOGLE_API_KEY = "SUA KEY DO API INSIRA AQUI"

2. Como Alterar o Tema (Prompt)<br>
O script é flexível. Para mudar o assunto do post ou o tom de voz da IA, localize a seção # Prompt de pesquisa no código:<br>
Onde mudar: Altere o texto dentro da variável prompt.

3. Como Alterar a Saída (Bloco de Notas)<br>
O resultado é salvo automaticamente em um arquivo de texto para garantir a persistência dos dados. Se você quiser mudar o nome do arquivo ou onde ele é salvo:<br>
Nome do arquivo: Localize a linha with open("dados-pesquisa.txt", "a", ...). Altere "dados-pesquisa.txt" para o nome que desejar (ex: "posts-linkedin.txt").<br>
Pasta de destino: Por padrão, o arquivo é criado na mesma pasta do script. Para salvar em outro lugar, insira o caminho completo (ex: C:\Users\Nome\Desktop\Pasta\arquivo.txt).

## 📂 Estrutura do Projeto

```text
pesquisa-automatizada/
│
├── Gerador-de-pesquisas-Gemini.py   # Script de geração de posts para o LinkedIn
├── Gerador-de-roteiros.py           # Script focado em estruturas de vídeo para YouTube
├── dados-pesquisa.json              # Banco/Histórico incremental de publicações geradas
├── roteiro_youtube_[DATA].md        # Roteiro em Markdown exportado individualmente por execução
├── .gitignore                       # Ignora ambientes virtuais (venv), variáveis locais (.env) e arquivos .txt
└── README.md                        # Documentação técnica do ecossistema 

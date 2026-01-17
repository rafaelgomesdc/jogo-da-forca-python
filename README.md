# 🎮 Jogo da Forca em Python (CLI)

Projeto de **Jogo da Forca desenvolvido em Python para execução no terminal**, com foco em **organização de código, arquitetura modular, lógica de negócio e boas práticas de desenvolvimento**.

O projeto foi estruturado para facilitar manutenção, testes e futuras evoluções, servindo como um **laboratório prático de aprendizado em Python**.

---

## 📌 Funcionalidades

- 🎯 Escolha aleatória de palavras
- 🧠 Sistema de dicas por categoria
- ❌ Controle de erros e condição de derrota
- 🏆 Verificação de vitória
- 🔤 Tratamento de letras acentuadas
- 🧪 Modo desenvolvedor para debug
- 🖥️ Interface de terminal organizada
- 🔄 Limpeza automática do terminal a cada rodada

---

## 🧠 Conceitos e Tecnologias Aplicadas

- Python 3
- Programação Orientada a Objetos (POO)
- Separação de responsabilidades (arquitetura modular)
- Estruturas de dados (listas)
- Controle de fluxo
- Pattern Matching (`match/case`)
- Validação de entrada do usuário
- Organização de projetos Python
- Importação entre módulos
- CLI (Command Line Interface)

---

## 📂 Estrutura do Projeto

```text
jogo-da-forca-python/
│
├── main.py                 # Ponto de entrada do jogo
│
├── game/
│   ├── __init__.py
│   ├── opcoes_dev          # Interface do modo desenvolvedor
│   ├── opcoes.py           # Lógica
│   ├── verificacao.py      # Lógica e validações
│   ├── menu.py             # Interface do terminal
│   ├── program.py          # Loop principal do jogo
│   └── palavra.py          # Modelo da palavra
│
├── data/
│   └── palavras.txt        # Base de palavras
│
└── README.md

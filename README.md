# Chatbot-Python
Chatbot com Python e json.

# 🤖 Chatbot de Atendimento Básico com Python (GUI)

Este é um projeto de chatbot simples desenvolvido em Python com interface gráfica para simular um atendimento ao cliente básico. O objetivo é demonstrar conceitos de processamento de linguagem natural (PLN) baseado em regras e a construção de interfaces gráficas com Tkinter.

---

## ✨ Funcionalidades

* **Reconhecimento de Intenções:** Identifica o propósito da pergunta do usuário (saudações, agradecimentos, horário de funcionamento, etc.).
* **Base de Conhecimento Externa:** Carrega perguntas e respostas de um arquivo `info_base.json` facilmente configurável.
* **Respostas Aleatórias:** Oferece variações nas respostas para a mesma pergunta, tornando a interação mais dinâmica.
* **Interface Gráfica (GUI):** Implementa uma janela interativa para a conversação, utilizando a biblioteca Tkinter.
* **Execução Não-Bloqueante:** Utiliza threads para garantir que a interface gráfica permaneça responsiva enquanto o chatbot processa a entrada.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Tkinter:** Para a construção da interface gráfica.
* **`re` (Regular Expressions):** Para o reconhecimento de padrões nas entradas do usuário.
* **`json`:** Para gerenciar a base de conhecimento.
* **`threading`:** Para processamento assíncrono.

---

## 🚀 Como Executar

1.  **Clone o Repositório:**
    ```
    git clone [https://github.com/vinifso/Chatbot-Python.git]

2.  **Certifique-se de ter o Python 3 instalado.**
3.  **Crie o arquivo `info_base.json`:**
    Baixe ou crie um arquivo `info_base.json` na raiz do projeto com o formato JSON de intenções e respostas (utilizando o formato igual ao do repositório).
4.  **Execute a Aplicação:**
    ```
    face.py

---


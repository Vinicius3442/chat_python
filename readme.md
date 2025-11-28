# Chatbot de TI | Assistente Virtual Python

![Banner do Projeto](img/banner.jpg)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-blue?style=for-the-badge&logo=python&logoColor=white)
![Badge Status](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=GREEN&style=for-the-badge)

<br>

> **Aplicação desktop robusta desenvolvida para o curso de Desenvolvimento de Sistemas (SESI/SENAI), simulando um assistente virtual com autenticação, temas dinâmicos e lógica de resposta.**

## Sobre o Projeto

Este projeto é um exercício prático de **Inteligência Artificial e Design de Interface**. O objetivo foi criar um chatbot funcional que operasse localmente, simulando o comportamento de uma IA de suporte técnico.

Diferente de scripts simples de terminal, esta aplicação conta com uma **Interface Gráfica (GUI)** completa construída nativamente com `Tkinter`, focando na experiência do usuário (UX) com troca de temas e feedback visual.

![Screenshot Principal](./img/chat_claro.jpg)
*Interface principal rodando no Modo Claro.*

---

## Funcionalidades Principais

### 1. Sistema de Autenticação
Segurança simulada para acesso ao sistema.
* **Conceitos:** Validação condicional, ocultamento de caracteres (senha).
* **Credenciais:** Usuário: `aluno` | Senha: `123`.

### 2. Lógica de Chat & Delay
O bot não responde instantaneamente, gerando uma sensação mais natural.
* **Conceitos:** `time.sleep` (simulação de raciocínio), Estruturas condicionais aninhadas.
* **Tópicos:** O bot reconhece palavras-chave sobre SQL, Redes, Hardware e Python.

### 3. Dark Mode Engine
Alternância de temas em tempo real sem reiniciar a aplicação.
* **Conceitos:** Manipulação de propriedades de widgets, gestão de estados de UI.
* **Visual:** Ajuste automático de fundo, fonte e caixas de entrada.

---

## Tecnologias e Conceitos Aplicados

### Engenharia de Software
* **Python 3:** Lógica core da aplicação.
* **Tkinter:** Construção da interface gráfica (Janelas, Frames, Entry, Scrollbar).
* **Lógica de Strings:** Tratamento de input do usuário (lower case, strip) para melhor reconhecimento de comandos.

---

## Galeria

<div align="center" style="display: flex; align-items: flex-start; justify-content: center;">
  <img src="./img/login.jpg" alt="Tela de Login" width="45%" style="margin: 5px;">
  <img src="./img/escuro.jpg" alt="Modo Escuro" width="45%" style="margin: 5px;">
</div>

---

# Autor

<div align="center">
  <a href="https://github.com/Vinicius3442">
    <img src="https://github.com/Vinicius3442.png" width="100px;" alt="Foto de Perfil do Vinícius Montuani" style="border-radius: 50%;"/>
  </a>

  <br />
  
  <h3>Vinícius Montuani</h3>

  <p>
    <em>Estudante de Desenvolvimento de Sistemas @ SENAI</em>
  </p>

  <br />

  <a href="https://www.linkedin.com/in/vinicius-montuani" target="_blank">
    <img src="https://img.shields.io/badge/-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge">
  </a>
  <a href="https://github.com/Vinicius3442" target="_blank">
    <img src="https://img.shields.io/badge/-GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Badge">
  </a>
</div>

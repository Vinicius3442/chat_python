import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

USUARIO_VALIDO = "aluno"
SENHA_VALIDA = "123"

TEMA_CLARO = {
    "COR_FUNDO": "#ECE5DD",
    "COR_BOTAO": "#075E54",
    "COR_TEXTO": "#000000",
    "COR_ENTRY": "#FFFFFF",
    "COR_FUNDO_CHAT": "#FEFEFE",
    "COR_MSG_USUARIO_BG": "#DCF8C6",
    "COR_MSG_BOT_BG": "#FFFFFF",
    "COR_NOME_USUARIO": "#075E54",
    "COR_NOME_BOT": "#888888"
}

TEMA_ESCURO = {
    "COR_FUNDO": "#121212",
    "COR_BOTAO": "#075E54",
    "COR_TEXTO": "#E0E0E0",
    "COR_ENTRY": "#2C2C2C",
    "COR_FUNDO_CHAT": "#1E1E1E",
    "COR_MSG_USUARIO_BG": "#056162",
    "COR_MSG_BOT_BG": "#2C2C2C",
    "COR_NOME_USUARIO": "#4FC3F7",
    "COR_NOME_BOT": "#B0B0B0"
}
FONT_FAMILIA = "Segoe UI"
FONT_TITULO = (FONT_FAMILIA, 18, "bold")
FONT_LABEL = (FONT_FAMILIA, 12)
FONT_TEXTO = (FONT_FAMILIA, 11)
FONT_BOTAO_GRANDE = (FONT_FAMILIA, 12, "bold")
FONT_BOTAO_PEQUENO = (FONT_FAMILIA, 10)
tema_atual = TEMA_CLARO

def tentar_login():
    usuario_digitado = entry_usuario.get()
    senha_digitada = entry_senha.get()

    if usuario_digitado == USUARIO_VALIDO and senha_digitada == SENHA_VALIDA:
        print("Login bem-sucedido!")
        frame_login.pack_forget()
        frame_chat.pack(fill="both", expand=True) 
        aplicar_tema()
        
        mensagem_boas_vindas = "Olá! Sou o Chatbot de TI. Faça uma pergunta sobre Python, IA, Hardware, Redes ou qualquer outro tópico de tecnologia."
        janela.after(500, lambda: inserir_texto_chat("Chatbot TI", mensagem_boas_vindas))
        
    else:
        messagebox.showerror("Erro de Login", "Usuário ou senha inválidos.")

def obter_resposta_bot(mensagem_usuario):
    msg = mensagem_usuario.lower()
    
    # --- Respostas Conversacionais (Small Talk) ---
    if "olá" in msg or "oi" in msg or "e aí" in msg:
        return "Olá! Sou um chatbot de TI. Como posso ajudar com Python, IA, GitHub ou outros tópicos?"
    elif "o que você sabe" in msg or "o que sabe" in msg or "tópicos" in msg or "quais são os tópicos" in msg or "sobre o que você fala" in msg:
        return ("Eu sou um especialista em TI! Posso falar sobre:\n"
                "  - Linguagens (Python, Java, C#, JS...)\n"
                "  - Web (HTML, CSS, React, Node.js...)\n"
                "  - Bancos de Dados (SQL, MySQL, MongoDB...)\n"
                "  - Cloud & DevOps (AWS, Azure, Docker...)\n"
                "  - Redes & Hardware (IP, DNS, CPU, SSD...)\n"
                "  - Conceitos (IA, API, Git, POO...)\n\n"
                "Me pergunte qualquer coisa sobre isso!")
    elif "bom dia" in msg:
        return "Bom dia! Pronto para começar a falar sobre tecnologia?"
    elif "boa tarde" in msg:
        return "Boa tarde! Em que posso te ajudar nesta tarde?"
    elif "boa noite" in msg:
        return "Boa noite! Buscando algumas respostas de TI antes de dormir?"
    elif "como você está" in msg or "tudo bem" in msg or "tudo certo" in msg:
        return "Estou 100% operacional e pronto para suas perguntas de TI! Meu código está rodando sem bugs."
    elif "quem é você" in msg or "o que você é" in msg:
        return "Eu sou um chatbot de TI, criado para um projeto do SESI/SENAI. Fui programado em Python com a biblioteca Tkinter!"
    elif "você é uma ia" in msg:
        return "Eu sou um sistema simulado! Minhas respostas são pré-programadas usando muitos `elif`s em Python. É um bom truque, né?"
    elif "você é real" in msg:
        return "Eu sou real...mente um bom script de Python! 😉"
    elif "seu nome" in msg:
        return "Pode me chamar de Chatbot TI. É um prazer!"
    elif "quem te criou" in msg or "quem te fez" in msg:
        return "Fui criado por um estudante muito inteligente do curso de Desenvolvimento de Sistemas do SESI/SENAI."
    elif "obrigado" in msg or "obrigada" in msg:
        return "De nada! Fico feliz em ajudar. Tem mais alguma dúvida?"
    elif "valeu" in msg:
        return "Disponha! Precisando, é só chamar."
    elif "tchau" in msg or "adeus" in msg or "até mais" in msg:
        return "Até logo! Foi um prazer ajudar. Bons estudos!"
    elif "me conta uma piada" in msg or "piada de ti" in msg:
        return "Quantos programadores são necessários para trocar uma lâmpada? Nenhum, isso é um problema de hardware!"
    elif "piada" in msg:
        return "O que o HTML disse para o CSS? 'Você me deixa muito mais bonito!'"
    elif "você pode me ajudar" in msg or "ajuda" in msg:
        return "Com certeza! Minha especialidade são assuntos de TI. O que você gostaria de saber?"
    
    # --- Tópicos Principais (Do seu código original) ---
    elif "python" in msg:
        return "Python é uma linguagem de programação de alto nível, interpretada, muito usada para web, ciência de dados e IA."
    elif "tkinter" in msg:
        return "Tkinter é a biblioteca padrão do Python para a criação de interfaces gráficas (GUI). Este app foi feito com ela!"
    elif "ia" in msg or "inteligência artificial" in msg:
        return "IA (Inteligência Artificial) é um campo da ciência da computação que foca na criação de máquinas inteligentes que podem simular o pensamento humano."
    elif "github" in msg:
        return "GitHub é uma plataforma de hospedagem de código-fonte e arquivos com controle de versão usando o Git. É essencial para trabalho em equipe."
    elif "sql" in msg:
        return "SQL (Structured Query Language) é uma linguagem padrão para gerenciar e manipular bancos de dados relacionais."

    # --- Linguagens de Programação ---
    elif "java " in msg or "java?" in msg:
        return "Java é uma linguagem de programação robusta e popular, muito usada para aplicações empresariais (backend) e desenvolvimento Android."
    elif "javascript" in msg or "js" in msg:
        return "JavaScript (JS) é a principal linguagem da web. Ela roda no navegador (frontend) e também no servidor (backend) com o Node.js."
    elif "c#" in msg or "c sharp" in msg:
        return "C# (C-Sharp) é uma linguagem moderna da Microsoft, muito usada para desenvolver aplicações Windows, serviços web com .NET e jogos com a engine Unity."
    elif "c++" in msg:
        return "C++ é uma linguagem de programação muito poderosa e rápida, usada para criar softwares que exigem alta performance, como jogos, motores gráficos e sistemas operacionais."
    elif "php" in msg:
        return "PHP é uma linguagem de script do lado do servidor muito popular para desenvolvimento web, sendo a base de sistemas como o WordPress."
    elif "swift" in msg:
        return "Swift é a linguagem de programação moderna da Apple para criar aplicativos para iOS, macOS, watchOS e tvOS."
    elif "kotlin" in msg:
        return "Kotlin é a linguagem de programação preferida pelo Google para o desenvolvimento de aplicativos Android modernos."
    elif "rust" in msg:
        return "Rust é uma linguagem conhecida por sua performance e, principalmente, pela segurança de memória, sendo usada para sistemas de baixo nível."
    elif "go" in msg or "golang" in msg:
        return "Go (ou Golang) é uma linguagem criada pelo Google, focada em simplicidade e eficiência, muito usada em backend e sistemas concorrentes."
    
    # --- Desenvolvimento Web (Frontend & Backend) ---
    elif "html" in msg:
        return "HTML (HyperText Markup Language) não é uma linguagem de programação, mas sim de marcação. Ela define a estrutura e o conteúdo de uma página web."
    elif "css" in msg:
        return "CSS (Cascading Style Sheets) é uma linguagem de estilo usada para definir a aparência (cores, fontes, layout) de uma página web feita em HTML."
    elif "react" in msg:
        return "React é uma biblioteca JavaScript criada pelo Facebook para construir interfaces de usuário (UI) de forma componenteizada e reativa."
    elif "angular" in msg:
        return "Angular é um framework completo de frontend, mantido pelo Google, usado para construir aplicações web complexas e de larga escala (SPAs)."
    elif "vue" in msg or "vue.js" in msg:
        return "Vue.js é um framework JavaScript progressivo, conhecido por ser fácil de aprender e muito flexível para construir interfaces de usuário."
    elif "node.js" in msg or "nodejs" in msg:
        return "Node.js é um ambiente que permite executar código JavaScript no lado do servidor (backend), ideal para construir APIs e microserviços."
    elif "frontend" in msg:
        return "Frontend é tudo o que o usuário vê e interage em uma aplicação (a interface). As principais tecnologias são HTML, CSS e JavaScript."
    elif "backend" in msg:
        return "Backend é a parte 'de trás' da aplicação que o usuário não vê. Envolve o servidor, o banco de dados e a lógica de negócios."
        
    # --- Bancos de Dados ---
    elif "mysql" in msg:
        return "MySQL é um dos sistemas de gerenciamento de banco de dados relacional (SQL) de código aberto mais populares do mundo."
    elif "postgresql" in msg:
        return "PostgreSQL é um banco de dados relacional de código aberto muito poderoso e avançado, conhecido por sua robustez e conformidade com padrões SQL."
    elif "mongodb" in msg:
        return "MongoDB é um banco de dados NoSQL (não-relacional) muito popular. Ele armazena dados em documentos flexíveis, parecidos com JSON."
    elif "nosql" in msg:
        return "NoSQL (Not Only SQL) é uma categoria de bancos de dados que não usam o modelo relacional tradicional. São ótimos para dados não estruturados e grande escala."

    # --- Cloud, DevOps e Ferramentas ---
    elif "cloud" in msg or "nuvem" in msg:
        return "Computação em Nuvem (Cloud) é a entrega de serviços de computação (servidores, armazenamento, IA) pela internet. Os maiores provedores são AWS, Azure e GCP."
    elif "aws" in msg:
        return "AWS (Amazon Web Services) é a plataforma de computação em nuvem da Amazon, a maior e mais antiga do mercado, oferecendo centenas de serviços."
    elif "azure" in msg:
        return "Microsoft Azure é a plataforma de nuvem da Microsoft, forte concorrente da AWS, com excelente integração com tecnologias Microsoft (.NET, etc)."
    elif "gcp" in msg or "google cloud" in msg:
        return "GCP (Google Cloud Platform) é a plataforma de nuvem do Google, muito conhecida por suas soluções de Big Data, Machine Learning e Kubernetes."
    elif "docker" in msg:
        return "Docker é uma plataforma que permite 'empacotar' uma aplicação e suas dependências em um 'contêiner', garantindo que ela rode igual em qualquer lugar."
    elif "kubernetes" in msg or "k8s" in msg:
        return "Kubernetes (ou K8s) é um sistema de 'orquestração' de contêineres. Ele gerencia e automatiza a execução de aplicações em contêineres Docker em larga escala."
    elif "git" in msg: # Deixei "git " (com espaço) para não confundir com "github"
        return "Git é um sistema de controle de versão distribuído. É uma ferramenta essencial para rastrear mudanças no código, reverter para versões antigas e trabalhar em equipe."
    elif "devops" in msg:
        return "DevOps é uma cultura e um conjunto de práticas que unem o Desenvolvimento de Software (Dev) e as Operações de TI (Ops), visando entregar software mais rápido e com mais qualidade."

    # --- Redes e Segurança ---
    elif "ip " in msg:
        return "Um Endereço IP (Internet Protocol) é um número único que identifica um dispositivo em uma rede, como o 'endereço' da sua casa na internet."
    elif "dns" in msg:
        return "DNS (Domain Name System) é o 'tradutor' da internet. Ele converte nomes fáceis de lembrar (como google.com) no endereço IP do servidor."
    elif "http" in msg or "https" in msg:
        return "HTTP é o protocolo para transferir dados na web. HTTPS (HyperText Transfer Protocol Secure) é a versão segura, que usa criptografia para proteger seus dados."
    elif "firewall" in msg:
        return "Um Firewall é uma barreira de segurança de rede que monitora e filtra o tráfego, decidindo o que pode entrar ou sair da sua rede, para bloquear ameaças."
    elif "vpn" in msg:
        return "VPN (Virtual Private Network) cria uma conexão segura e criptografada pela internet, como um 'túnel privado', para proteger sua privacidade e dados."
    
    # --- Conceitos Gerais de TI ---
    elif "api" in msg:
        return "API (Application Programming Interface) é um conjunto de regras que permite que diferentes sistemas de software 'conversem' e troquem informações entre si."
    elif "ide" in msg:
        return "IDE (Ambiente de Desenvolvimento Integrado) é um software que agrupa ferramentas para programadores, como editor de código, depurador e compilador. Ex: VS Code."
    elif "vs code" in msg or "visual studio code" in msg:
        return "O Visual Studio Code (VS Code) é um editor de código-fonte gratuito e muito popular da Microsoft. É leve, rápido e extensível."
    elif "poo" in msg or "oop" in msg or "orientada a objetos" in msg:
        return "POO (Programação Orientada a Objetos) é um paradigma de programação baseado no conceito de 'objetos', que contêm dados (atributos) e código (métodos)."
    elif "framework" in msg:
        return "Um Framework é uma estrutura de código pré-pronta que oferece uma base para construir aplicações. Ele define 'como' o app deve ser estruturado. Ex: Angular, Django."
    elif "biblioteca" in msg or "library" in msg:
        return "Uma Biblioteca (Library) é um conjunto de funções e códigos prontos que você pode 'chamar' no seu programa para realizar tarefas específicas. Ex: React, Tkinter."
    elif "bug" in msg or "erro" in msg:
        return "Um 'bug' é um erro, falha ou defeito em um programa de computador que faz com que ele se comporte de forma inesperada ou incorreta."
        
    # --- Hardware e Sistemas Operacionais ---
    elif "linux" in msg:
        return "Linux é um sistema operacional de código aberto (open-source) muito popular. É a base da maioria dos servidores do mundo e também do Android."
    elif "windows" in msg:
        return "Windows é o sistema operacional gráfico da Microsoft, o mais usado em computadores pessoais (desktops e notebooks) no mundo."
    elif "macos" in msg:
        return "macOS é o sistema operacional desenvolvido pela Apple para sua linha de computadores Macintosh (Mac)."
    elif "android" in msg:
        return "Android é o sistema operacional móvel do Google, baseado em Linux, usado na maioria dos smartphones e tablets do mundo (exceto os da Apple)."
    elif "ios" in msg:
        return "iOS é o sistema operacional móvel da Apple, usado exclusivamente em seus dispositivos: o iPhone, iPad (iPadOS) e iPod Touch."
    elif "cpu" in msg or "processador" in msg:
        return "CPU (Unidade Central de Processamento) é o 'cérebro' do computador. É o componente que executa as instruções e cálculos de todos os programas."
    elif "ram" in msg or "memória ram" in msg:
        return "Memória RAM (Random Access Memory) é a memória de 'trabalho' do computador. Ela é super rápida e armazena os dados que estão sendo usados ativamente (programas abertos)."
    elif "ssd" in msg:
        return "SSD (Solid State Drive) é um tipo de dispositivo de armazenamento moderno que usa memória flash (sem partes móveis). É muito mais rápido que um HD tradicional."
    elif "hd" in msg or "disco rígido" in msg:
        return "HD (Hard Disk) é o dispositivo de armazenamento tradicional, que usa discos magnéticos giratórios para gravar dados. É mais lento, mas oferece mais espaço por um preço menor."

    else:
        return "Desculpe, não entendi. Meus tópicos principais são de TI (Tecnologia da Informação). Pode tentar perguntar sobre Python, Cloud, Hardware ou outro tópico?"
    
def inserir_texto_chat(remetente, mensagem):
    caixa_chat.config(state="normal")
    
    if remetente == "Usuário":
        tag_nome = "usuario_nome"
        tag_msg = "usuario_msg"
        tag_alinhamento = "align_right"
        nome_texto = "👤 Você:\n" #
    else:
        tag_nome = "bot_nome"
        tag_msg = "bot_msg"
        tag_alinhamento = "align_left"
        nome_texto = "🤖 Chatbot TI:\n" #

    linha_inicio = caixa_chat.index(tk.END).split('.')[0] + ".0"

    caixa_chat.insert(tk.END, nome_texto, tag_nome)

    caixa_chat.insert(tk.END, f"{mensagem}\n\n", tag_msg)

    linha_fim = caixa_chat.index(tk.END)

    caixa_chat.tag_add(tag_alinhamento, linha_inicio, linha_fim)

    caixa_chat.config(state="disabled")
    caixa_chat.see(tk.END)

def enviar_mensagem():
    msg_usuario = entry_mensagem.get()
    
    if msg_usuario.strip() == "":
        return

    inserir_texto_chat("Usuário", msg_usuario)

    entry_mensagem.delete(0, tk.END)
    
    resposta = obter_resposta_bot(msg_usuario)
    
    janela.after(1000, lambda: inserir_texto_chat("Chatbot TI", resposta))

def limpar_conversa():
    caixa_chat.config(state="normal")
    caixa_chat.delete(1.0, tk.END)
    caixa_chat.config(state="disabled")
    print("Conversa limpa.")

def configurar_tags_chat():
    global tema_atual


    for tag in ["usuario_nome", "usuario_msg", "bot_nome", "bot_msg", "align_right", "align_left"]:
        caixa_chat.tag_delete(tag)

    caixa_chat.tag_configure("align_right", 
                             justify=tk.RIGHT, 
                             lmargin1=50, lmargin2=50, rmargin=10)
                             
    caixa_chat.tag_configure("align_left", 
                             justify=tk.LEFT, 
                             lmargin1=10, lmargin2=10, rmargin=50)

    # Bloco Usuário
    caixa_chat.tag_configure("usuario_nome", 
                             font=(FONT_FAMILIA, 10, "bold"),
                             background=tema_atual["COR_MSG_USUARIO_BG"],
                             foreground=tema_atual["COR_NOME_USUARIO"],
                             spacing1=5)
    caixa_chat.tag_configure("usuario_msg", 
                             font=FONT_TEXTO, 
                             background=tema_atual["COR_MSG_USUARIO_BG"],
                             foreground=tema_atual["COR_TEXTO"],
                             spacing3=10,
                             wrap=tk.WORD)
    
    caixa_chat.tag_configure("bot_nome", 
                             font=(FONT_FAMILIA, 10, "bold"),
                             background=tema_atual["COR_MSG_BOT_BG"],
                             foreground=tema_atual["COR_NOME_BOT"],
                             spacing1=5) 
    caixa_chat.tag_configure("bot_msg", 
                             font=FONT_TEXTO,
                             background=tema_atual["COR_MSG_BOT_BG"],
                             foreground=tema_atual["COR_TEXTO"],
                             spacing3=10,
                             wrap=tk.WORD)

def aplicar_tema():
    global tema_atual
    
    fundo = tema_atual["COR_FUNDO"]
    texto = tema_atual["COR_TEXTO"]
    botao_bg = tema_atual["COR_BOTAO"]
    entry_bg = tema_atual["COR_ENTRY"]
    chat_bg = tema_atual["COR_FUNDO_CHAT"]

    janela.config(bg=fundo)

    frame_login.config(bg=fundo)
    label_titulo.config(bg=fundo, fg=botao_bg)
    label_usuario.config(bg=fundo, fg=texto)
    entry_usuario.config(bg=entry_bg, fg=texto, insertbackground=texto)
    label_senha.config(bg=fundo, fg=texto)
    entry_senha.config(bg=entry_bg, fg=texto, insertbackground=texto)
    
    frame_chat.config(bg=fundo)
    frame_entrada_botoes.config(bg=fundo)
    entry_mensagem.config(bg=entry_bg, fg=texto, insertbackground=texto)
    frame_opcoes.config(bg=fundo)
    
    botao_limpar.config(bg=entry_bg, fg=texto)
    botao_tema.config(bg=entry_bg, fg=texto)
    
    botao_login.config(cursor="hand2")
    botao_enviar.config(cursor="hand2")
    botao_limpar.config(cursor="hand2")
    botao_tema.config(cursor="hand2")

    caixa_chat.config(bg=chat_bg)
    
    configurar_tags_chat()

def alternar_tema():
    global tema_atual
    
    if tema_atual == TEMA_CLARO:
        tema_atual = TEMA_ESCURO
        print("Mudando para TEMA ESCURO")
    else:
        tema_atual = TEMA_CLARO
        print("Mudando para TEMA CLARO")
        
    aplicar_tema()


janela = tk.Tk()
janela.title("Chatbot SESI/SENAI")
janela.geometry("500x700") 
janela.configure(bg=TEMA_CLARO["COR_FUNDO"])

# --- Fase 1: Tela de Login ---
frame_login = tk.Frame(janela, bg=TEMA_CLARO["COR_FUNDO"])
frame_login.pack(pady=100, padx=20, fill="both", expand=True) 

label_titulo = tk.Label(frame_login, text="Login - Chatbot TI", 
                        font=FONT_TITULO,
                        bg=TEMA_CLARO["COR_FUNDO"], fg=TEMA_CLARO["COR_BOTAO"])
label_titulo.pack(pady=20)

label_usuario = tk.Label(frame_login, text="Usuário:", font=FONT_LABEL, bg=TEMA_CLARO["COR_FUNDO"])
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(frame_login, font=FONT_LABEL, width=30, bg=TEMA_CLARO["COR_ENTRY"], relief=tk.FLAT)
entry_usuario.pack(pady=5, ipady=5)

label_senha = tk.Label(frame_login, text="Senha:", font=FONT_LABEL, bg=TEMA_CLARO["COR_FUNDO"])
label_senha.pack(pady=5)
entry_senha = tk.Entry(frame_login, font=FONT_LABEL, width=30, show="*", bg=TEMA_CLARO["COR_ENTRY"], relief=tk.FLAT)
entry_senha.pack(pady=10, ipady=5)

botao_login = tk.Button(frame_login, text="Entrar", 
                        font=FONT_BOTAO_GRANDE,
                        command=tentar_login,
                        bg=TEMA_CLARO["COR_BOTAO"], fg="white", 
                        width=15, relief=tk.FLAT, borderwidth=0)
botao_login.pack(pady=20, ipady=5)

frame_chat = tk.Frame(janela) 

caixa_chat = scrolledtext.ScrolledText(frame_chat, 
                                       wrap=tk.WORD, 
                                       font=FONT_TEXTO,
                                       state="disabled",
                                       borderwidth=0, relief=tk.FLAT) 
caixa_chat.pack(pady=10, padx=10, fill="both", expand=True)

configurar_tags_chat()

frame_entrada_botoes = tk.Frame(frame_chat)
frame_entrada_botoes.pack(fill="x", padx=10, pady=(0, 10))

entry_mensagem = tk.Entry(frame_entrada_botoes, 
                          font=FONT_LABEL,
                          borderwidth=0, relief=tk.FLAT) 
entry_mensagem.grid(row=0, column=0, sticky="ew", padx=(0, 10), ipady=10) 
frame_entrada_botoes.grid_columnconfigure(0, weight=1) 

botao_enviar = tk.Button(frame_entrada_botoes, 
                         text="Enviar", 
                         font=FONT_BOTAO_PEQUENO,
                         bg=TEMA_CLARO["COR_BOTAO"], fg="white",
                         command=enviar_mensagem,
                         borderwidth=0, relief=tk.FLAT, padx=15)
botao_enviar.grid(row=0, column=1, ipady=8)

frame_opcoes = tk.Frame(frame_chat)
frame_opcoes.pack(fill="x", padx=10, pady=(0, 10))

botao_limpar = tk.Button(frame_opcoes, 
                         text="Limpar", 
                         font=FONT_BOTAO_PEQUENO,
                         command=limpar_conversa,
                         borderwidth=0, relief=tk.FLAT)
botao_limpar.pack(side="left", padx=5)

botao_tema = tk.Button(frame_opcoes, 
                       text="Alternar Tema", 
                       font=FONT_BOTAO_PEQUENO,
                       command=alternar_tema,
                       borderwidth=0, relief=tk.FLAT)
botao_tema.pack(side="left", padx=5)

aplicar_tema()

# --- Loop Principal da Aplicação ---
janela.mainloop()
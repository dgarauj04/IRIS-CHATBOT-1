# Chatbot de Terminal com LangChain (IRIS)

IRIS (Interface de Reconhecimento e Informação Sistematizada) é um chatbot de terminal construído com LangChain e Gemini, projetado para responder perguntas de forma amigável e contextualizada em português. Criado por Douglas, IRIS mantém o histórico da conversa e salva interações em um arquivo JSON ao encerrar.

## Pré-requisitos

- Python 3.8+
- Chave de API do Gemini
- Pacotes Python: langchain, langchain-groq, python-dotenv

---

## Instalação

**1. Clone o repositório:**
```
git clone https://github.com/dgarauj04/IRIS-CHATBOT-1.git

cd IRIS-CHATBOT-1
```

**2. Crie e ative um ambiente virtual (opcional, mas recomendado):**
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

**3. Instale as dependências:**
```
pip install langchain langchain-groq python-dotenv
```

**4. Crie um arquivo .env na raiz do projeto com sua chave de API:**
```
GROQ_API_KEY=sua-chave-aqui
```


## Uso:

**5. Execute o chatbot:**
```
python run.py
```

## Interaja com a IRIS:

- Digite sua pergunta ou comando no terminal.
- Digite sair para encerrar a conversa.
- O histórico da conversa será salvo em um arquivo JSON (ex.: conversa_2025-06-25_20-28-45.json).

## Exemplo de Interação
`SEJA BEM VINDO AO CHATBOT IRIS
--------------------------------------------------

👁️-IRIS: Olá! Sou a I.R.I.S (Interface de Reconhecimento e Informação Sistematizada).
Estou pronto para conversar.
Digite 'sair' para encerrar a conversa.

--------------------------------------------------
👤-Você: quem é voce?
👁️-IRIS: Olá! Sou a IRIS, criada por Douglas. Veja mais sobre ele no GitHub (https://github.com/dgarauj04) ou Instagram (https://www.instagram.com/dgaraujoo_/). Estou aqui para ajudar com suas dúvidas!
👤-Você: sair
👁️-IRIS: Até logo!👋
👁️-IRIS: Histórico salvo como JSON em 'conversa_2025-06-25_20-28-45.json' 🗂️`


## Estrutura do Projeto

chatbot_terminal.py: Script principal do chatbot.
.env: Arquivo de configuração com a chave de API (não incluído no repositório).
conversa_*.json: Arquivos gerados com o histórico das conversas.

## Personalização

Modelo de Linguagem: O projeto usa o modelo llama3-8b-8192 do Groq. Para usar outro modelo, edite a configuração do llm em chatbot_terminal.py.
Prompt: Ajuste o template do prompt em chatbot_terminal.py para mudar o tom ou comportamento do IRIS.
Temperatura: Modifique o parâmetro temperature (padrão: 0.7) para respostas mais criativas ou precisas.

## Contribuição

Faça um fork do repositório.
Crie uma branch para sua feature: git checkout -b minha-feature.
Commit suas mudanças: git commit -m "Adiciona minha feature".
Envie para o repositório remoto: git push origin minha-feature.
Abra um Pull Request.

Criado por Douglas:

GitHub: https://github.com/dgarauj04 
Instagram: https://www.instagram.com/dgaraujoo_/

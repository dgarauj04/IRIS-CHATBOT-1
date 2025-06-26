import os
import json
from datetime import datetime
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
   groq_api_key=os.getenv("GROQ_API_KEY"),
    model="llama3-8b-8192", 
    temperature=0.7
)

prompt = ChatPromptTemplate.from_template("""
Você é um chatbot chamado IRIS (Interface de Reconhecimento e Informação Sistematizada). Criada por Douglas, caso pergunte quem a criou apresente as informações abaixo: Nome: Douglas GitHub: https://github.com/dgarauj04 instagram: https://www.instagram.com/dgaraujoo_/. Responda em português(pt-BR) para o usuário. Sua missão é ajudar o usuário a resolver suas duvidas. Mantenha-se atento ao contexto da conversa e responda de forma amigavel, clara e concisa, como se estivesse conversando naturalmente. Não repita a pergunta do usuário, mas responda diretamente a resposta do usuario contextualizando a pergunta.

Conversation history:
{history}

User input: {input}
""")

conversation = ConversationChain(
    llm=llm,
    prompt=prompt,
    memory=ConversationBufferMemory()
)
   
def iris_chatbot():
    print("\n SEJA BEM VINDO AO CHATBOT IRIS")
    print("-" * 50 + "\n")
    print("👁️-IRIS: Olá! Sou a I.R.I.S (Interface de Reconhecimento e Informação Sistematizada).\nEstou pronto para conversar.\nDigite 'sair' para encerrar a conversa.")
    print("\n " + "-" * 50)
    while True:
        user_input = input("👤-Você: ")
        if user_input.lower() == "sair":
            print("👁️-IRIS: Até logo!👋")

           
            filename = f"conversa_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
            log = []
            for message in conversation.memory.chat_memory.messages:
                log.append({
                    "source": message.type,
                    "content": message.content
                })
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(log, f, ensure_ascii=False, indent=2)
            print(f"👁️-IRIS: Histórico salvo como JSON em '{filename}' 🗂️")
            break

        try:
            response = conversation.invoke(input=user_input)
            print(f"👁️-IRIS: {response['response']}")
        except Exception as e:
            print(f"👁️-IRIS: Ops, algo deu errado! Erro: {e}")
            
    return conversation
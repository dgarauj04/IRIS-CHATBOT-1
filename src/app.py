import os
import json
from datetime import datetime
from google import genai
from google.genai import types
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

# IMPORTANT: KEEP THIS COMMENT - Using python_gemini integration
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

app = Flask(__name__, template_folder='../templates')

# Armazenar histórico de conversas na memória (em produção, use um banco de dados)
conversation_history = []

def get_iris_response(user_input: str) -> str:
    """
    Gera resposta da IRIS usando Gemini
    """
    system_prompt = """
Você é um chatbot chamado IRIS (Interface de Reconhecimento e Informação Sistematizada). 
Criada por Douglas, caso pergunte quem a criou apresente as informações abaixo: 
Nome: Douglas 
GitHub: https://github.com/dgarauj04 
Instagram: https://www.instagram.com/dgaraujoo_/

Responda sempre em português brasileiro (pt-BR) para o usuário. 
Sua missão é ajudar o usuário a resolver suas dúvidas. 
Mantenha-se atento ao contexto da conversa e responda de forma amigável, clara e concisa, 
como se estivesse conversando naturalmente. 
Não repita a pergunta do usuário, mas responda diretamente contextualizando a pergunta.
"""
    
    # Construir contexto da conversa
    context = "\n".join([f"Usuário: {msg['user']}\nIRIS: {msg['assistant']}" for msg in conversation_history[-5:]])
    
    prompt = f"{system_prompt}\n\nHistórico da conversa:\n{context}\n\nUsuário: {user_input}\nIRIS:"
    
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash-latest",
            contents=prompt
        )
        return response.text or "Desculpe, não consegui processar sua mensagem."
    except Exception as e:
        # Log the error for debugging (in production, use proper logging)
        print(f"Error generating response: {e}")
        return "Desculpe, não consegui processar sua mensagem no momento. Tente novamente."
   
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({'error': 'Mensagem vazia'}), 400
    
    # Gerar resposta da IRIS
    iris_response = get_iris_response(user_message)
    
    # Adicionar ao histórico
    conversation_history.append({
        'user': user_message,
        'assistant': iris_response,
        'timestamp': datetime.now().isoformat()
    })
    
    return jsonify({
        'response': iris_response,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/history')
def get_history():
    return jsonify(conversation_history)

@app.route('/download_history')
def download_history():
    filename = f"conversa_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(conversation_history, f, ensure_ascii=False, indent=2)
    return jsonify({'message': f'Histórico salvo como {filename}', 'filename': filename})

@app.route('/health')
def health_check():
    """Health check endpoint for deployment monitoring"""
    try:
        # Test basic functionality
        status = "healthy"
        timestamp = datetime.now().isoformat()
        
        # You can add more health checks here in the future
        # For example: database connection, external API status, etc.
        
        return jsonify({
            'status': status,
            'timestamp': timestamp,
            'service': 'IRIS Chatbot',
            'version': '1.0.0'
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'error': 'Health check failed',
            'timestamp': datetime.now().isoformat()
        }), 503

def create_app():
    return app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
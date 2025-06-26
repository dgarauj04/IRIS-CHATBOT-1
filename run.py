#INICIAR O NOSSO SERVIDOR
from src.app import iris_chatbot

app = iris_chatbot()

if __name__ == '__main__':
    app.run(debug=True)
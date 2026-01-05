Projeto API de Usuários (Django REST Framework)
Este é um projeto de estudo de um CRUD completo.

🚀 Como rodar o projeto
Clone este repositório.

Crie um ambiente virtual: python -m venv venv.

Instale as dependências: pip install -r requirements.txt.

Rode as migrações: python manage.py migrate.

Inicie o servidor: python manage.py runserver.

🛠 Como testar o DELETE/PUT (Métodos que você criou)
Como o navegador não envia corpos de requisição por padrão, utilize o Postman ou Thunder Client:

URL: http://127.0.0.1:8000/api/data/

Método: DELETE (ou PUT)

Corpo (JSON): > ```json { "user_nickname": "pauloaz" }

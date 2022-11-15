<h1 align="center">Gerenciador de Projetos</h1>

Criação de um microserviço que gerencia a criação e edição de um cartão de visita digital QR-CODE, a partir de aplicação API.

## 🛠️ Ferramentas e Tecnologias

- Python 3
- IDE: Visual Studio Code
- Flask - framework web usado
- SQLAlchemy - conexão com banco de dados SQLite

## ⚙ Funcionalidades

- Lista de usuários
- Informações sobre um usuário em específico
- Cadastro de novo usuário
- Atualização de cadastro
- Remoção de usuários
- Relação entre usuários e projetos
- Geração de QR-CODE

## 💻 Como executar o projeto

Antes de iniciar a aplicação é necessário a instalação das seguintes ferramentas: Python, Git e IDE de sua preferência. Além disso, a criação do banco de dados "project_manager" no MySQL.

- Clone esse repositório:

  ```$ git clone <https://github.com/ViniciusRaony/projeto_qr_code.git>```

- Crie uma variável de ambiente para criação do Banco de Dados: 

  ```DATABASE_URL = mysql://login:senha@localhost:3306/nomeDoBancoDeDados (Exemplo com MySQL)```

- Instale as dependências:

  ```$ pip install -r requirements.txt```

- Execute a aplicação:
 
  ```$ python3 app.py```

- URL para acessar servidor local:

  ```acesse http://localhost:5000/``` 


## 🚉 Rotas da API


- Rota ```/user``` (método ```GET```): Retorna todos usários cadastrados na API

- Rota ```/user/id``` (método ```GET```): Retorna um usário cadastrado na API baseado no ```id```

- Rota ```/user``` (método ```POST```): Cria um cadastro de usuário na API

- Rota ```/user/id``` (método ```PUT```): Atualiza um cadastro de usuário na API baseado no ```id```

- Rota ```/user/id``` (método ```DELETE```): Deleta um cadastro de usuário na API baseado no ```id```

### Links úteis

- [Documentação Flask: https://flask.palletsprojects.com ](https://flask.palletsprojects.com)
- [Documentação SQLAlchemy: https://flask-sqlalchemy.palletsprojects.com/en/2.x/](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)



### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com)

É bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/).

Qualquer banco de dados com compatibilidade com o [SQLAchelmy](https://sqlalchemy.org/) pode ser utilizado.

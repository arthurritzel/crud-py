# CRUD com Django e MySQL

![GitHub](https://img.shields.io/github/issues/arthurritzel/crud-py)
![GitHub](https://img.shields.io/github/forks/arthurritzel/crud-py)
![GitHub](https://img.shields.io/github/stars/arthurritzel/crud-py)

Este repositório contém um exemplo de aplicativo CRUD (Create, Read, Update, Delete) desenvolvido em Python com o framework Django e utiliza o banco de dados MySQL para armazenar os dados. O CRUD permite gerenciar recursos por meio de uma interface web.

## Descrição

Este projeto é um exemplo básico de como criar um CRUD com Django e MySQL. O Django é um framework web Python de alto nível que facilita o desenvolvimento de aplicativos web, incluindo a criação de modelos de banco de dados e a construção de interfaces web.

## Funcionalidades

O CRUD oferece as seguintes funcionalidades básicas:

- **Listar Recursos**: Visualize todos os recursos existentes no banco de dados.

- **Adicionar Recursos**: Crie novos recursos por meio de um formulário web.

- **Atualizar Recursos**: Edite informações de recursos existentes usando um formulário web.

- **Excluir Recursos**: Remova recursos do banco de dados.

## Pré-requisitos

- Python 3.x instalado
- Django instalado
- MySQL instalado e configurado (com um banco de dados vazio criado)

## Configuração

1. Clone este repositório:

   ```bash
   git clone https://github.com/arthurritzel/crud-py.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd crud-py
   ```

3. Configure o banco de dados MySQL em `settings.py`:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'seu_banco_de_dados',
           'USER': 'seu_usuario',
           'PASSWORD': 'sua_senha',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

4. Execute as migrações para criar as tabelas no banco de dados:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## Uso

1. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

2. Abra seu navegador e acesse o aplicativo em [http://localhost:8000](http://localhost:8000).

Agora você pode usar o CRUD para criar, listar, atualizar e excluir recursos no banco de dados MySQL.

**Desenvolvido por [Arthur Ritzel]**

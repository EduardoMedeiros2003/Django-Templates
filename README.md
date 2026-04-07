🚀 Django Templates Project

This is a web application built with Django, focused on template organization, reusable components, and best development practices.
Eduardo Space is a web application built with Django that simulates a dynamic image gallery focused on space photography. The project evolved from a simple template-based application into a full-featured system with authentication, search, and CRUD operations.
This project demonstrates practical backend development skills using Django, including database modeling, user authentication, and dynamic content rendering.

---

## 📌 About the project

The goal of this project is to apply important Django concepts such as:

- Project structure organization
- Separation of concerns
- Code reusability
- Static files management

The application simulates an image gallery with navigation between pages.

---

## ⚙️ Technologies used

- Python
- Django
- HTML5
- CSS3

---

## 🧠 Features implemented

🔐 Authentication System

User registration with validation

Login with authentication

Logout functionality

Access control (only authenticated users can access content)

🖼️ Image Gallery

Dynamic rendering of images

Image detail page

Fallback image when no image is available

Ordering by most recent images

🔎 Search System

-Search images by name
-Case-insensitive filtering
-Dynamic rendering of results

⚙️ Admin Panel (CRUD)

-Full management via Django Admin
-Create, edit, delete, and view images
-Filters and search inside admin
-Inline editing of publication status

🧾 Forms & Validation

-Django Forms implementation
Custom validations:
-No spaces in username
-Password confirmation check
-Error handling with user feedback
💬 Messaging System
-Success and error messages using Django messages framework

🏗️ Tech Stack

-Python 3
-Django 5
-SQLite (default database)
-HTML5
-CSS3
-Bootstrap 5
-------
🚀 How to run the project

bash
# Clone the repository
git clone <your-repository>

# Navigate to the project folder
cd project

# Create virtual environment
python -m venv venv

# Activate environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python manage.py runserver
---------------------------------------------------------------------------------------------------------------------------------------------------------
🚀 Projeto Django Templates

Este é um projeto web desenvolvido com Django, com foco na organização de templates, reutilização de componentes e boas práticas de desenvolvimento.
Eduardo Space é uma aplicação web desenvolvida com Django que simula uma galeria dinâmica de imagens focada em fotografias do espaço. O projeto evoluiu de uma aplicação simples baseada em templates para um sistema completo com autenticação, busca e operações de CRUD.
Este projeto demonstra habilidades práticas de desenvolvimento backend com Django, incluindo modelagem de banco de dados, autenticação de usuários e renderização dinâmica de conteúdo.

---

## 📌 Sobre o projeto

O objetivo deste projeto é aplicar conceitos importantes do Django, como:

- Estruturação de projetos
- Separação de responsabilidades
- Reutilização de código
- Organização de arquivos estáticos

A aplicação simula uma galeria de imagens com navegação entre páginas.

---

## ⚙️ Tecnologias utilizadas

🔐 Sistema de Autenticação
-Cadastro de usuários com validações
-Login com autenticação
-Funcionalidade de logout
-Controle de acesso (somente usuários autenticados acessam o conteúdo)
🖼️ Galeria de Imagens
-Renderização dinâmica das imagens
-Página de detalhes da imagem
-Imagem padrão quando não há imagem disponível
-Ordenação por imagens mais recentes
🔎 Sistema de Busca
-Busca de imagens por nome
-Filtro case-insensitive
-Renderização dinâmica dos resultados
⚙️ Painel Administrativo (CRUD)
-Gerenciamento completo via Django Admin
-Criar, editar, excluir e visualizar imagens
-Filtros e busca no admin
-Edição rápida do status de publicação
🧾 Formulários e Validações
-Implementação com Django Forms
-Validações personalizadas:
-Não permitir espaços no nome de usuário
-Confirmação de senha
-Tratamento de erros com feedback ao usuário
💬 Sistema de Mensagens
-Mensagens de sucesso e erro utilizando o framework de messages do Django
🏗️ Tecnologias Utilizadas
-Python 3
-Django 5
-SQLite (banco de dados padrão)
-HTML5
-CSS3
-Bootstrap 5
---

🚀 Como executar o projeto

bash
- Clonar o repositório
git clone <seu-repositorio>

- Entrar na pasta
cd projeto

- Criar ambiente virtual
python -m venv venv

- Ativar ambiente (Windows)
venv\Scripts\activate

- Instalar dependências
pip install -r requirements.txt

- Rodar servidor
python manage.py runserver

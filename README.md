**Descrição:**

Este projeto foi desenvolvido durante a Pystack Week 13 com foco em desenvolvimento web utilizando Django. A plataforma tem como objetivo facilitar o gerenciamento de processos de mentoria, permitindo que usuários se cadastrem, criem perfis de mentores e mentorados, e organizem agendamentos de forma segura e eficiente.

**Funcionalidades:**

- Cadastro e login de usuários com validação
- Criação de mentores
- Mentores podem cadastrar mentorados
- Geração de token único de acesso para cada mentorado
- Validação de tokens de acesso
- Agendamento de horários com controle de disponibilidade
- Página exclusiva para mentorados acessarem horários via token
- Upload de arquivos

**Tecnologias utilizadas:**

- Python
- Django
- HTML / Tailwind css
- SQLite

**Como executar o projeto localmente**

Pré-requisitos:
- Python 3.10+ instalado
- Virtualenv (opcional, mas recomendado)

**Passo a passo**

1️⃣ Clone o repositório

```
git clone https://github.com/luis-otavio-dias/projeto-gerenciamento.git
cd projeto-gerenciamento
```

2️⃣ Crie um ambiente virtual e instale as dependências

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3️⃣ Configure o banco de dados

No arquivo settings.py configure o banco de dados em DATABASES.

O SQLite já estará configurado por padrão.

4️⃣ Aplique as migrações

```
python manage.py migrate
```

5️⃣ Crie um superusuário para acessar o painel administrativo

```
python manage.py createsuperuser
```

6️⃣ Inicie o servidor local

```
python manage.py runserver
```
Agora, acesse http://127.0.0.1:8000/ no navegador.

**Contribuição**

Se quiser contribuir, fique à vontade para abrir issues ou enviar um pull request!


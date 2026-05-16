# Deepora

O Deepora é uma plataforma de organização de estudos desenvolvida com Django.

O objetivo do projeto é ajudar estudantes a organizarem sua rotina de estudos, acompanharem seu progresso e criarem consistência através de métricas e sessões registradas.

---

# Funcionalidades

* Cadastro e autenticação de usuários
* Criação de matérias
* Registro de sessões de estudo
* Controle de tempo estudado
* Dashboard com métricas
* Sequência de estudos (streak)
* Organização pessoal de estudos

---

# Tecnologias Utilizadas

## Backend

* Python
* Django 6

## Banco de Dados

* PostgreSQL
* Supabase

## Deploy

* Render

## Frontend

* HTML
* CSS
* Django Templates

---

# Preview

> Em breve screenshots do sistema.

---

# Rodando Localmente

## 1. Clone o repositório

```bash
git clone https://github.com/seuusuario/deepora.git
```

---

## 2. Entre na pasta

```bash
cd deepora
```

---

## 3. Crie um ambiente virtual

### Windows

```bash
python -m venv .venv
```

### Linux/macOS

```bash
python3 -m venv .venv
```

---

## 4. Ative o ambiente virtual

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

---

## 5. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 6. Configure as variáveis de ambiente

Crie um arquivo `.env`:

```env
SECRET_KEY=sua_secret_key
DEBUG=True
DATABASE_URL=sua_database_url
```

---

## 7. Rode as migrações

```bash
python manage.py migrate
```

---

## 8. Inicie o servidor

```bash
python manage.py runserver
```

---

# Estrutura do Projeto

```txt
accounts/   -> autenticação e usuários
core/       -> páginas principais
studies/    -> lógica de estudos
templates/  -> templates HTML
static/     -> arquivos estáticos
```

---

# Roadmap

* [ ] Relatórios avançados
* [ ] Sistema Pomodoro
* [ ] Metas de estudo
* [ ] Gráficos de desempenho
* [ ] Sistema de tarefas
* [ ] Tema dark mode
* [ ] Banco de questões
* [ ] IA para análise de desempenho

---

# Status do Projeto

🚧 Em desenvolvimento.

---

# Licença

Este projeto está sob a licença MIT.

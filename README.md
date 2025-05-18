# projeto-ci-api
Claro! Com base na estrutura visível na sua imagem, aqui está um modelo de `README.md` adequado para o seu projeto `projeto-ci-cd`, que usa Flask com MySQL e Docker Compose:

---

```markdown
# Projeto CI/CD com Flask, MySQL e Docker

Este é um projeto simples que demonstra a integração de uma API Python (Flask) com um banco de dados MySQL utilizando Docker e Docker Compose. O projeto também prepara o ambiente para futuras implementações de CI/CD.

## 📁 Estrutura do Projeto

```

projeto-ci-cd/
│
├── app.py                  # Código principal da aplicação Flask
├── init.sql                # Script SQL de criação do banco e tabela
├── Dockerfile              # Dockerfile da aplicação web
├── docker-compose.yml      # Orquestração dos containers
├── requirements.txt        # Dependências da aplicação Python
└── README.md               # Este arquivo

````

## 🚀 Como Executar

### Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Passo a passo

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/projeto-ci-cd.git
cd projeto-ci-cd
````

2. Construa e suba os containers:

```bash
docker-compose up --build
```

3. Acesse a API:

* **GET todos os itens**: `http://localhost:5000/items`
* **POST um novo item**: `http://localhost:5000/items`

### Exemplo de corpo para POST:

```json
{
  "name": "Item de Exemplo"
}
```

## 🧱 Banco de Dados

* O banco de dados é iniciado com:

  * Nome do banco: `flaskdb`
  * Tabela: `items` com colunas `id` e `nome`
  * Dados iniciais inseridos via `init.sql`

## 🐳 Docker

* O serviço `db` utiliza a imagem oficial do MySQL.
* O serviço `web` constrói a aplicação Flask definida no `Dockerfile`.
* O `init.sql` é usado para inicializar o banco automaticamente.

## 🛠 Tecnologias Utilizadas

* Python + Flask
* MySQL
* Docker + Docker Compose

---

## 📫 Contato

Caso tenha dúvidas ou sugestões, sinta-se à vontade para abrir uma issue ou entrar em contato.

```

---

```

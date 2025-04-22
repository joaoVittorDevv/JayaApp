# Conversor de Moedas - Django

Este projeto foi desenvolvido para realizar conversões de moedas usando uma API construída com Django. O projeto utiliza [django-cookiecutter](https://github.com/cookiecutter/cookiecutter-django), que fornece uma estrutura Dockerizada pronta para deploy e diversas configurações opcionais.

## Tecnologias utilizadas

- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)

## Estrutura do Projeto

A estrutura gerada pelo django-cookiecutter é modular e organizada. As principais pastas são:

### `jayaapp`
- `auth`: Configuração personalizada para autenticação e obtenção de tokens.
- `transactions`: Contém os arquivos referentes ao aplicativo responsável pelas conversões e listagens.
- `users`: Modelo que estende o usuário padrão do Django para uso na API.

### `config`
Contém as configurações gerais do projeto Django e as rotas definidas.

## Como rodar o projeto

Para executar o projeto localmente com Docker, siga os passos abaixo:

1. Crie um arquivo `.env` dentro da pasta `.envs/.local/` com o seguinte conteúdo:

```dotenv
USE_DOCKER=yes
IPYTHONDIR=/app/.ipython
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_DB=jayaapp
POSTGRES_USER=cGZPNYUdOHIdCDubBRlILGZzoxmpSQFT
POSTGRES_PASSWORD=srdO2HpgbfDMnmTzoiOKzvMRc0gbxf7yq6NErL8XDlOCbyHAgFzsetVwninor7oN
DATABASE_URL=postgres://cGZPNYUdOHIdCDubBRlILGZzoxmpSQFT:srdO2HpgbfDMnmTzoiOKzvMRc0gbxf7yq6NErL8XDlOCbyHAgFzsetVwninor7oN@postgres:5432/jayaapp
EXCHANGE_API_KEY=<sua_chave_da_api>
```
As credenciais do banco de dados PostgreSQL devem ser mantidas exatamente como estão acima, pois os containers Docker foram configurados para usar essas credenciais localmente.
Já a variável EXCHANGE_API_KEY deve ser substituída pela sua chave de acesso à API de conversão de moedas.

2. Após criar o arquivo `.env`, execute os comandos:

```bash
docker-compose build
docker-compose up
```

Isso irá construir os containers e iniciar os serviços da aplicação. A API estará disponível em http://localhost:8000/.

## Endpoints da API

A API disponibiliza três endpoints principais:

### Autenticação

`POST /api/auth-token/`

Utilizado para obter tokens de acesso com os parâmetros `username` e `password`. O usuário padrão é:

- **Username:** `admin`
- **Password:** `admin`

Novos usuários podem ser cadastrados através do [Django Admin](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/), acessado com as mesmas credenciais acima.

### Conversão de Moedas

`POST /api/transactions/conversion/`

Realiza a conversão de valores entre moedas. Requisição JSON:

```json
{
   "user_id": "123",
   "origin_currency": "BRL",
   "origin_value": 100,
   "destination_currency": "USD"
}
```
### Conversão de Moedas

`POST /api/transactions/conversion/`

Retorna uma lista de todas as operações realizadas pelo usuário autenticado com o token.

### Documentação Swagger

O sistema também disponibiliza uma documentação interativa via Swagger no seguinte endpoint:

`GET /api/docs/`

> Essa rota é gerada automaticamente utilizando o `SpectacularSwaggerView` e permite testar os endpoints diretamente pela interface web.


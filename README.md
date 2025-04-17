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

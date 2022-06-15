# Teste Zappts (Magic The Gathering)

## Apresentação

Este documento é para apresentar o funcionamento da implementação das rotas para cadastro de um jogo de cartas chamado Magic the Gathering. Foi realizado em python tendo como principal framework FastAPI.

OBS: Tive dificuldade ao realizar o deploy, não é do meu usual fazer o mesmo.

## Autenticação

Está sendo usado nesta API a rota de proteção JWT. Logo,
para o acesso/autenticação da mesma será necessário entrar na rota:

```url
/docs
```

Entrando em "/Docs", na requisição POST de Login,:
```json
{
    "username": "zappts@teste.com",
    "password": "zappts",
}
```
RETORNO:

```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ6YXBwdHNAdGVzdGUuY29tIiwiZXhwIjoxNjU1MzA5MDE2fQ.BIdYjV0fnSB_SJupQKCb7Lgst5rosZcdi8IYSlnrHC8",
    "token_type": "bearer"
}
```
Ao ter o token em mãos é necessário ir em authorization no campo Type seleciona " BEARER TOKEN " e colar o token no campo.

## Começando

Para acessar a api serão necessários os seguites requisitos:

- [Python 3.9: necessário para a execução do sistema](www.python.org/)
- [Postman: necessário para o teste da API](www.postman.com)

## Desenvolvimento

Para o inicio do desenvolvimento, será necessário clonar o projeto do github em seu diretório.

```commandline
mkdir "diretório_de_sua_preferência"
cd "diretório_de_sua_preferência"
git clone https://github.com/CelsoBNF/fastapi
```

## Construção

Para iniciar a construção da API, execute os comandos abaixo em sua pasta do projeto.

Para ambiente Unix
```commandline
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirement.txt
```

Para ambiente Windows
```commandline
pip install virtualenv
virtualenv venv
venv/Scripts/activate.bat
pip install -r requirements.txt
```
Este comando instalará todos os módulos necessários para este projeto.


### Carta
Nesta rota conseguimos cadastrar, listar, buscar, modificar e deletar uma carta na API

POST - Para cadastrar uma nova carta
```url
/card
```

BODY:
```json
{
    "name": "Calculating Lich",
  "edition": "Menace",
  "language": "EN",
  "foil": "No",
  "price": 80,
  "quantity": 1
}
```
RETORNO:

```json
{
    "edition": "Menace",
  "name": "Calculating Lich",
  "foil": "No",
  "quantity": 1,
  "id": 4,
  "language": "EN",
  "price": 80,
  "user_id": 1
}
```
GET - Para listar todas as cartas

```url
/card
```

RETORNO:

```json
{
    [
  {
    "player": {
      "name": "string",
      "email": "string",
      "cards": []
    },
    "name": "string",
    "edition": "string",
    "language": "string",
    "foil": "string",
    "price": 0,
    "quantity": 0
  }
]
}
```
GET by Name - Para buscar uma carta especifica (Pelo nome).
```url
/card/{name}
```
RETORNO:
```json
{
    "player": {
    "name": "Celso",
    "email": "zappts@teste.com",
    "cards": [
      {
        "name": "teste1",
        "edition": "teste2",
        "language": "teste3",
        "foil": "teste4",
        "price": 0,
        "quantity": 0
      },
      {
        "name": "teste2",
        "edition": "teste3",
        "language": "string",
        "foil": "string",
        "price": 0,
        "quantity": 0
      },
}
```

PUT - Para atualizar uma carta. Esta rota precisa estar logada para funcionar
```url
/card/{id}
```
BODY:
```json
{
    "name": "changename",
  "edition": "string",
  "language": "string",
  "foil": "string",
  "price": 0,
  "quantity": 0
}
```
RETORNO:

```json
{
    "id": 1
    "name": "changename",
  "edition": "string",
  "language": "string",
  "foil": "string",
  "price": 0,
  "quantity": 0
}
```


DELETE - Para apagar uma carta. Esta rota precisa estar logada para funcionar

```url
/card/{id}
```
RETORNO:
```json
{
    "message": "done"
}
```

## Testes
Lembrando que o banco de dados deve estar criado. Caso não esteja execute o seguinte comando:

## Safe gás

## Tecnologias utilizadas

- Django 
- Python 
- Django-Rest-Framework
- Django Channels
- Paho Mqtt
- Docker
- PostgreSQL
- Simple-JWT
- Ionic 



## Metodologias e Padrões
- PEP 8 Guideline para o código Python.


## Instalação


### Requisitos

- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/) (Linux)
- [Docker Desktop](https://www.docker.com/products/docker-desktop) (Windows e Mac)
- [Docker Compose](https://docs.docker.com/compose/) (Linux, Windows e Mac)
- [Node Js](https://nodejs.org/en) (Linux, Windows e Mac)
- [Inic](https://ionicframework.com/)

# FRONTEND 

```bash
# Instale as dependências
cd frontend

npm install

ionic serve
```

# BACKEND 


```bash
# Instale as dependências
cd backend

docker compose up --build
# apos a instalacao rode o script Python que estabelece o tunel entre o broker e o app

cd backend/mqtt-config 

python core.py

```




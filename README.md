# FastAPI based HTTP endpoint template

## Overview

This repo contains a simple "hello world" example of an API built with [FastAPI](https://fastapi.tiangolo.com/). 

## Setup

- [source](https://fastapi.tiangolo.com/#installation)
```
python3 -m venv venv
```

```
pip install -r requirements.txt
```


## Apps

This repo contains a simple app: `app/main.py`

This contains endpoints:
- root of API:
```
GET http://127.0.0.1:8000
```
- create a new order:
```
POST http://127.0.0.1:8000/user/{user_id}/order
```

- get all users orders:
```
GET http://127.0.0.1:8000/user/{user_id}/orders
```

## Run App

```
fastapi dev app/main.py
```

```
fastapi dev app/hello_fastapi.py
```

API Docs: http://127.0.0.1:8000/docs

## Run tests
[testing](https://fastapi.tiangolo.com/tutorial/testing/)
```
pytest app/test_main.py
```

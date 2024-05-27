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

This repo contains a simple app: `app/hello_fastapi.py`

This contains endpoints:
- GET http://127.0.0.1:8000
- GET http://127.0.0.1:8000/items/{item_id}
- PUT http://127.0.0.1:8000/items/{item_id}


The repo also contains a more complete app: `app/main.py`

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

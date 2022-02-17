## Installation
<div class="termy">

Activate virtual environment
```console
$ virtualenv env
$ cd env/Scripts
$ activate
```
Install the tools needed

```console
$ pip install fastapi pymysql sqlalchemy uvicorn
```
## Code
<div class="termy">

## Run it
Run the server:
<div class="termy">

```console
$ uvicorn index:app --reload
```
```
(env) .\fastapi>uvicorn index:app --reload
INFO:     Will watch for changes in these directories: ['\\fastapi']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [49336] using statreload
INFO:     Started server process [43372]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## Swagger API documentation

```console
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
```




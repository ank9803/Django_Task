# README

## Requirements
* `python` 3.8
* `pip`
* [`virtualenv`](https://virtualenv.pypa.io/en/latest/)

## Activate virtual environment
```sh
$ source venv/bin/activate
```

## Manage dependencies in virtual environment
```sh
$ (venv) pip install -r requirements.txt
```

## Apply Migrations 
```sh
$ (venv) python manage.py makemigrations
```

## Migrate Changes
```sh
$ (venv) python manage.py migrate
```

## For running the task
```sh  
$ (venv) python manage.py runserver
```

## Open Url In Browser
```sh  
http://127.0.0.1:8000/employee/get/
```

## Run TestCases
```sh  
$ (venv) python manage.py test
```

## Note: Some Time this API show `HTTP Error 429: Too Many Requests` due to fetching data from 3rd party API
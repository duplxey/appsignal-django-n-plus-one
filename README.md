# appsignal-django-n-plus-one

This repository contains the codebase for the article [Find and Fix N+1 Queries in Django using AppSignal](#).

It is split into two branches:

1. `base` -- serves as a starting point to follow the article
2. `master` -- contains the final codebase after fixing the N+1 problems

## Development Setup

1. Fork/Clone

1. Create and activate a virtual environment:

    ```sh
    $ python3 -m venv venv && source venv/bin/activate
    ```

1. Install the requirements:

    ```sh
    (venv)$ pip install -r requirements.txt
    ```

1. Apply the migrations:

    ```sh
    (venv)$ python manage.py migrate
    ```

1. Populate the database:

    ```sh
    (venv)$ python manage.py populate_db
    ```

1. Create a *.env* file with the following contents:

    ```sh
    APPSIGNAL_PUSH_API_KEY=<your_push_api_key>
    ```

1. Run the server:

    ```sh
    (venv)$ python manage.py runserver
    ```
   
1. Navigate to [http://localhost:8000/](http://localhost:8000/) in your browser. N+1 problematic endpoints are:

   1. `books/`
   1. `books/by-author`
   1. `admin/books/author/1/change/`

## Superuser

The superuser credentials after populating the database are:

```
user: admin
pass: password
```

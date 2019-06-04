# Django Vue Template ✌️ 🐍

This template is a minimal example for an application using Vue and Django.

It's setup to have a clear separation: use Vue, Yarn, and Webpack to handle all frontend logic and assets bundling,
and use Django with Django REST framework to manage a Data Models, Web API, and serve static files.

While it's possible to add endpoints to serve django-rendered html responses, the intention is to use Django primarily for the backend, and have view rendering and routing and handled by Vue + Vue Router as a Single Page Application (SPA).

Out of the box, Django will serve the application entry point (`index.html` + bundled assets) at `/` ,
data at `/api/`, and static files at `/static/`. Django admin panel is also available at `/admin/` and can be extended as needed.

The application templates from Vue CLI `create` and Django `createproject` are kept as close as possible to their
original state, except where a different configuration is needed for better integration of the two frameworks.


### Includes

* Django
* Django REST framework
* Django Whitenoise, CDN Ready
* Vue CLI 3
* Vue Router
* Vuex
* Gunicorn
* Configuration for Heroku Deployment


### Template Structure


| Location             |  Content                                   |
|----------------------|--------------------------------------------|
| `/backend`           | Django Project & Backend Config            |
| `/backend/api`       | Django App (`/api`)                        |
| `/src`               | Vue App .                                  |
| `/src/main.js`       | JS Application Entry Point                 |
| `/public/index.html` | Html Application Entry Point (`/`)         |
| `/public/static`     | Static Assets                              |
| `/dist/`             | Bundled Assets Output (generated at `yarn build` |

## Prerequisites

Before getting started you should have the following installed and running:

- [X] Yarn - [instructions](https://yarnpkg.com/en/docs/install)
- [X] Vue CLI 3 - [instructions](https://cli.vuejs.org/guide/installation.html)
- [X] Python 3 - [instructions](https://wiki.python.org/moin/BeginnersGuide)
- [X] Pipenv - [instructions](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv)

## Setup Template

```
$ git clone https://github.com/gtalarico/django-vue-template
$ cd django-vue-template
```

Setup
```
$ yarn install
$ pipenv install --dev && pipenv shell
$ python manage.py migrate
```

## Running Development Servers

```
$ python manage.py runserver
```

From another tab in the same directory:

```
$ yarn serve
```

The Vue application will be served from [`localhost:8080`](http://localhost:8080/) and the Django API
and static files will be served from [`localhost:8000`](http://localhost:8000/).

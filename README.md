## <b>Stack</b>
### <b>backend</b>
 * Python
   * FastAPI
   * Pydantic
   * SQLAlchemy
   * Psycopg
   * Alembic
   * PyJWT
 * PostgreSQL

### <b>frontend</b>
 * Vue 
   * vue/cli@5.0.8
   * vue@3.2.13
   * vue-router@4.0.3
   * axios@1.7.7
   * vuex@4.1.0
   * bootstrap@5.3.3

## <b>Project structure</b>

    ├── README.md  
    ├── .gitignore
    ├── docker-compose.yml  
    ├── backend
    │   ├── .gitignore
    │   ├── alembic.ini
    │   ├── docker.env
    │   ├── Dockerfile
    │   ├── pipfile
    │   ├── pipfile.lock
    │   ├── alembic
    │   │   ├── env.py
    │   │   ├── README.txt
    │   │   ├── script.py.mako
    │   │   └── versions
    │   ├── src
    │   │   ├── config.py
    │   │   ├── server.py
    │   │   ├── crypto
    │   │   │   └── crypto.py
    │   │   ├── database
    │   │   │   ├── models
    │   │   │   └── repositories
    │   │   ├── entities
    │   │   └── routers
    └── frontend
        ├── .gitignore
        ├── Dockerfile
        ├── README.md
        ├── babel.config.js
        ├── jsconfig.json
        ├── package-lock.json
        ├── package.json
        ├── vue.config.js
        ├── public
        │   ├── favicon.ico
        │   └── index.html
        ├── src
        │   ├── App.vue
        │   ├── main.js
        │   ├── assets
        │   │   └── logo.png
        │   ├── components
        │   │   └── HelloWorld.vue
        │   ├── main.js
        │   ├── router
        │   │   └── index.js
        │   └── views
        │       ├── AboutView.vue
        │       └── HomeView.vue

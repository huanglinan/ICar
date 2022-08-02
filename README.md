# ICar


Quickstart
----------
for running the backend server locally
- first install 
```bash
pip install fastapi uvicorn sqlalchemy sqlalchemy_utils psycopg2 python-dotenv
```
- run the local server with localhost:8080
```bash
cd /ICarService
uvicorn main:app
```

for running the web server 
- first install 
```bash
npm install -g @angular/cli@11.2.19
```
- then install pakages 
```bash
cd /ICarApp
npm i
```

- run the local server with localhost:4200
```bash
npm s
```


for PostgreSQL you might like to change user/password to conenct the DB server to do this go to
- open ICarSevice/.env

and change those config
```bash
DB_USER = postgres
DB_PASSWORD = postgres
DB_NAME = db_icar
DB_ADRESS = localhost
```

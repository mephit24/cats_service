The application is realisation test task for job interview: https://github.com/wgnet/wg_forge_backend

## For start application:

* You must have installed PostgreSQL:  
https://www.postgresql.org/download/

* Create demonstartion database (ex. 'cats') and structure by 'original_db.sql', being in application directory.  

* Clone application from Github:
  ```bash
  git clone https://github.com/mephit24/cats_service.git
  ```
  Or download it:
  https://github.com/mephit24/cats_service/archive/refs/heads/main.zip
* Go to app directory:
  ```bash
  cd /path/to/app
* Run only for first time:
  ```bash
  python3 -m pip install -r requirements.txt
* Run:
  ```bash
  python3 run.py
* Options of database connection:
  --host |
  --database |
  --user |
  --password
* Use options or configure file 'config.json' for set database connect.
* Open url http://localhost:8080/ping in your internet browser. 
## For start application in Docker:

* Install Docker and docker-compose:  
  + https://docs.docker.com/engine/install  
  + https://docs.docker.com/compose/install

* Clone application from Github:
  ```bash
  git clone https://github.com/mephit24/cats_service.git
  ```
  Or download it:
  https://github.com/mephit24/cats_service/archive/refs/heads/main.zip

* Go to app directory:
  ```bash
  cd /path/to/app
* Run: 
  ```bash
  docker-compose build
  docker-compose up
  ```
  (Application will be run on forwarded to your host 8081 port.)
* Open url http://localhost:8081/ping in your internet browser.  

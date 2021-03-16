# Simple Flask Application

**Application to demonstrate flask integration with redis via. API**

Steps to run the application

### Approach 1: Without Docker

Prerequisite: To be installed on computer
1. Python 3
2. Redis 

Step 1: Clone the repo
$ git clone <repo-url>

Step 2: Create Python Virutal Environment
$ python3 -m venv venv

Step 3: Activate Virtual Environment
$ source venv/bin/activate

Step 4: Cd to project dir
$ cd <repo-name>

Step 5: Install Dependencies
$ pip install -r requirements.txt

Step 6: Start Redis
Start a new terminal to run redis server
$ redis-server

Step 7: Start Application
$ python app.py


### Approach 2: With Docker

Prerequisite: To be installed on computer
1. Docker
2. Docker Compose

Step 1: Run docker compose commmand
$ docker-compose up -d



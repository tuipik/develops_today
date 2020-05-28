# develops_today
***A simple news board API.***

---
**Usage**

- Install docker and git on your machine

- Clone this repository via http `git clone https://github.com/tuipik/develops_today.git`
or via ssh `git clone git@github.com:tuipik/develops_today.git`

- In terminal open directory with source code of repo

- Build or pull docker image. In terminal: `make build` or `make pull`

- Start local server by `make run` command in Terminal

- Fill up database with testing data and superuser `make db`

    to login with superuser use login: `test_user`  password: `test_pass`
 
- To start tests use command `make test`
---
**Endpoints:**

deployed

create user: `http://18.191.196.119:8000/api/v1/createuser/`

post: `http://18.191.196.119:8000/api/v1/post/`

comment: `http://18.191.196.119:8000/api/v1/comment/`

upvote: `http://18.191.196.119:8000/api/v1/post/1/upvote` 
  
==
local

create user: `http://0.0.0.0:8000/api/v1/createuser/`

posts list: `http://0.0.0.0:8000/api/v1/post/`

post detail: `http://0.0.0.0:8000/api/v1/post/1`

post upvote: `http://0.0.0.0:8000/api/v1/post/1/upvote`

comments list: `http://0.0.0.0:8000/api/v1/comment/`

comment detail: `http://0.0.0.0:8000/api/v1/comment/1`

---
**Postman Collections** 
 
local: `https://www.getpostman.com/collections/93e19b4679a8b256229d`

deploy: `https://www.getpostman.com/collections/8915400b44f20e7cd6b5`
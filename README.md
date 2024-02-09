<h1>Microservice-with-Python</h1>
<p>To run the project you make sure you have python installed</p>
<p>Follow the following steps to run the project</p>
<hr>
<h2>Backend</h2>
-admin - written in django
-to install packages run pip install -r requirements.txt
-main - written in flask
-to install packages run pip install -r requirements.txt

Docker should be installed in your machine 
To build docker file run docker compose up it will build a docker container 

the database container will build and rabbitmq management

Admin will listen to port 8000
Flask app main will listen to 8001

Database will listen to port 33066 to access the database 
Rabbitmq will listen to port 15672 to access rabbitmq UI

Access the django container and run django migrations
Access the flask container and run flask migrations



Frontend 
run nmp install to install packages 
npm start to start the project

# Microservice-with-Python

This project is a microservice-based application written in Python. It consists of a backend and a frontend component. The backend is divided into two services: admin, which is built using Django, and main, which is built using Flask. The frontend is built using a JavaScript framework.

## Prerequisites
Before running the project, make sure you have the following prerequisites installed:
- Python
- Docker
- Node.js (for the frontend)

## Backend Setup
1. Install the required Python packages by running the following command in the terminal: pip install -r requirements.txt
2. Build the Docker container by running the following command:docker-compose up
   
This will build the Docker container for the backend services and also set up the database container and RabbitMQ management.

4. The admin service will be accessible on port 8000, and the Flask app (main service) will be accessible on port 8001.

5. To access the database, use port 33066.

6. RabbitMQ can be accessed through port 15672.

7. Access the Django container and run the Django migrations.

8. Access the Flask container and run the Flask migrations.

## Frontend Setup
1. Install the required Node.js packages by running the following command in the terminal:

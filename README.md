# Sample microservices architecture using python flask and sql alchemy

## Global architecture

There are two services:
* Movies: allows to manage movie informations. Each movie has two attributes: the movie name and its release year. The service is implemented as a REST API. All required requests are implemented.
* Evaluations: allows to manage the movie evaluations. Each movie can have any number of evaluation. An evaluation has two attributes: the description and the evaluated movie id. The service is implemented as a REST API. All required requests are implemented.

Each service interacts with its own database.

The two services interact through HTTP protocol for some of the requests.

## Single host dev deployment

To deploy the application on a single host for development purposes, follow the instructions in the file: **local_deployment.md**.


## Deploy using Docker, Gunicorn and MySQL
To deploy the microservices app using docker service using  gunicorn as application server on a single host, follow the instructions
in the file **docker_deployment.md**.


## Multi-host, multi instance deployment using swarm and compose
To deploy the microservices app on multiple hosts, using multiple instances for each service, follow the instructions
in the file **swarm_deployment.md**.

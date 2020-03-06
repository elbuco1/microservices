# Sample microservices architecture using python flask and sql alchemy

# Docker deployment
## Deploy using Docker, Gunicorn and MySQL
To deploy the microservices app using docker service using  gunicorn as application server
and mysql server. 
* Install docker: https://docs.docker.com/install/linux/docker-ce/ubuntu/
* Install docker-compose: https://docs.docker.com/compose/install/

* Clone repository: <code>$ git clone https://github.com/elbuco1/microservices.git</code>
* Go in the **microservices** directory: <code>$ cd microservices</code>
* Go in **movies/config.py** and **evaluations/config.py** and set
```python
class Config(object):
    deploy = 'docker'
```
* To start the evaluations micro-service run:

<code>$ sudo docker-compose up evaluations </code>
or 
<code>$ sudo docker-compose up -d evaluations </code> 

to run the containers in the background.

You can find the service on "http://127.0.0.1:8081/evaluations"

* To start the movies micro-service run:

<code>$ sudo docker-compose up movies </code>
or 
<code>$ sudo docker-compose up -d movies </code> 

to run the containers in the background.

You can find the service on "http://127.0.0.1:8080/movies"

To test the communication between the two services go to: "http://127.0.0.1:8081/evaluations/movies/1"

You should get the following json:

```python
    { 'evaluations':
        {
            0:{
                description:"What a baaad movie!"
                id:1
                movie_id:1
            }
        }	
    }
```


## Stopping all docker containers:

To shutdown the app:
<code>$ sudo docker-compose down</code> 

To stop all containers:
<code>$ sudo docker stop $(sudo docker ps -a -q)</code> 

To remove all containers:

<code>$ sudo docker rm $(sudo docker ps -a -q)</code> 




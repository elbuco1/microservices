ifconfig 

enp0s31f6:  ...
        inet 132.207.72.45  ...
            ...




#on manager:
sudo docker swarm init --advertise-addr 132.207.72.45

#on worker-i:
sudo docker swarm join --token SWMTKN-1-2asjk309buj3a9yyz8i1krh9xvgqb6ykhzbkjfk9frraeya5k8-e2iowjdf7msjjqda2oxwomagm 132.207.72.45:2377


# Create a local registry for images
sudo docker service create --name registry --publish published=5000,target=5000 registry:2

# Test registry 
curl http://localhost:5000/v2/


# Building images for swarm 
sudo docker-compose -f docker-compose-swarm.yml up -d --build

# List containers
sudo docker-compose ps

# Test app 
curl http://localhost:8081/evaluations/movies/1

# expected result: 
# {"evaluations":[{"description":"What a baaad movie!","id":1,"movie_id":1}]}

# shut down the app 
sudo docker-compose down --volumes

# push images to the local registry 
sudo docker-compose -f docker-compose-swarm.yml push

# deploy stack on the swarm
sudo docker stack deploy --compose-file docker-compose-swarm.yml stack

# check deployment
sudo docker stack services stack


# Test app 
curl http://localhost:8081/evaluations/movies/1

# expected result: 
# {"evaluations":[{"description":"What a baaad movie!","id":1,"movie_id":1}]}

# see on what node the service is deployed
sudo docker service ps stack_db_evaluations
sudo docker service ps stack_movies
sudo docker service ps stack_db_movies
sudo docker service ps stack_evaluations


# update service:
# find id:  
sudo docker stack services stack
# update:
sudo docker service update --force <ID>







# stop stack
sudo docker stack rm stack

# stop local registry 
sudo docker service rm registry


# leave swarm

#on manager:
sudo docker swarm leave --force

#on worker-i:
sudo docker swarm leave 
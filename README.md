# pythonMongodb
It is a demo of flask application running in one container that can query to MongoDB running in 
another container. 
Note: My host machine on which docker is installed is Ubuntu 20.04

For this project we have:
 i. app.py, where we have defined our Database and the authentication user to fetch the values stored in our database.
 ii. init-db.js, where we have provided the database values.
 iii. Dockerfile, where we have instructed to install python and some of it's supporting packages/modules.
 iv. docker-compose.yml, where we have instructed to install mongodb and set it's environment. Also here we have exposed the required port and linked app with db.
 v. modules.txt, file where we have defined our python modules to be installed. 

Requirements
1. First install docker (https://hub.docker.com/search/?type=edition&offering=community), in my case Docker version 20.10.2, build 2291f61
2. Install docker compose:
- curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
 i. Adds executable permission to the docker compose binary file
-  chmod +x /usr/local/bin/docker-compose
 ii. Ensure docker compose is installed on your host machine:
- docker-compose --version
3. Build the environmet and run application with docker-compose up.
4. Go to your Web-browser and type "http://machine's_ip_address:5000"
- this will show us our landing page 
5. On your same browser type "http://machine's_ip_address:5000/contents" to see the values that are extracted from our 
MongoDB.
	

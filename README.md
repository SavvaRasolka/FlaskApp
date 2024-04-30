# Flask App

This is test app with simple REST API implementation. App using MongoDB.

## Install

Clone the project
```bash
git clone https://github.com/SavvaRasolka/FlaskApp.git
cd FlaskApp
```

## Run

Before running, create .env file in root directory. The .example file provides example that runs app on 8080 port.
Follow these steps to set up Docker and Docker Compose for your project.

1. **Install Docker**

   Make sure you have the latest version of Docker installed on your system.

2. **Install Docker Compose**

   Refer to this [link](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-centos-7) for instructions on how to install Docker Compose.

3. **Update Docker Compose**

   Run the following commands to update Docker Compose to the latest version:

   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```
   
4. **docker-compose.yml**

   Download or create 'docker-compose.yml' file in directory you want to start docker.
   
5. **Start Docker Services**

   Open a terminal in the directory where the 'docker-compose.yml' file is located using the 'cd' command.
   Execute the following command to start the Docker services defined in the docker-compose.yml file:
   ```bash
   docker-compose up
   ```

## Endpoints

### GET /products

This request is used to retrieve all objects. Server will respond with list of objects.

### POST /products

This request is used to post object. Requests body should have an object as json. The object will be added if there are no same keys. Return status 400 if such key is present.

### GET /products/<key>

This request is used to retrieve object with <key>. Returns empty list if there is no such key.

### PUT /products/<key>

This request is used to put object with <key>. Returns status 400 if there is no <key> or there is object with key, that same as key in object from requests body. Requests body should have an object as json.

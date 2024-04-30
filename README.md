# Flask App

This is test app with simple REST API implementation.

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

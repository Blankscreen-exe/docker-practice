# Use VSCode inside a docker container for development

## How to Set Up?

### Step 1: Create a custom image with your code

You will need a **custom image** which contains your source code. You can even do this with and empty folder but then there will be no application to try it out with.

Create a `Dockerfile` with configurations for your custom image. Here are the things you need to keep in mind before initiating the `build` command:

- [ ] Select a working directory
- [ ] Install dependencies
- [ ] Copy source code into the container
- [ ] Run the app

These are the basic stuff. After making sure of the above list build your custom image.

```ssh
docker build -t <image_name> . 
```

Make sure the container doesn't stop immediately after it runs. For this you need to write a command to run the application which will be enclosed inside the container. An example for this is given in the `Dockerfile`.

> 📌 Installing program dependencies may have problems with `ssl` config.
> If you get something like this during your `docker build` operation ...
> 
> `Retrying (Retry(total=4, connect=None, read=None, redirect=None)) after connection broken by 'ProtocolError('Connection aborted.', gaierror(-2, 'Name or service not known'))': /simple/fast-api/`
> 
> look [here](https://stackoverflow.com/questions/28668180/cant-install-pip-packages-inside-a-docker-container-with-ubuntu) for a possible solution

### Step 2: Configure Docker File Sharing Paths to recognize your Volume path

You can only create volumes where the `path` is registered with docker engine.

**Do it through Docker Desktop**

Inside [Docker Desktop](https://www.docker.com/products/docker-desktop/) go to the following location:

```shell
settings -> Resources -> File Sharing
```

Once you are there you will see a prompt to add new paths to be recoignized as `Volumes`.

**Do it through Docker CLI**

List out the current direcotries recognized by docker

```shell
docker info --format '{{.DockerRootDir}}'
```

It works if the directory you want is inside the directory listed in the results. If you cannot find your source code path inside this list edit the `filesharingDirectories` key in the docker `deamon.json`.

```shell
# exclusively for ubuntu
sudo nano /etc/docker/daemon.json
```

A good command line tutorial for container file sharing can be found [here](https://www.digitalocean.com/community/tutorials/how-to-share-data-between-docker-containers-on-ubuntu-22-04)

### Step 3: Instantiate a container out of the custom image

Run your container with port and volume mapping. 

```shell
docker run --name <container_name> -d -v <host_directory>:<container_directory> -p <host_port>:<container_port> <image_name>
```

Check if the volumes are mapped correctly by making some changes in the `host_directory` to see that the app running on `host_port` reflects successfully.

### Step 4: Connect VS Code to running container

You need a VS Code extension for this purpose.

[<img src="https://img.shields.io/badge/Remote_Explorer_VSCode_Extension-%23A0DDF1.svg?&style=for-the-badge&logo=visual-studio-code&logoColor=gray" alt="Remote Explorer">](https://marketplace.visualstudio.com/items?itemName=ms-vscode.remote-explorer)

```shell
ext install ms-vscode.remote-explorer
```

After installing it, select any running containers and attach it to current or new window to start the IDE.

### By using Docker Compose

While writing your docker compose script, make sure to add the following under the `app` service name

```yml
services:
  app:

    ...
  
    volumes:
      - .:/code

    ...
```
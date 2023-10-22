[⬅️ Back to repo home](https://github.com/Blankscreen-exe/docker-practice) ▪️ [↗️ Back to search](https://blankscreen-exe.github.io/docker-practice/)

# Dockerize Simple Python Script

I have dockerized a simple python script which only prints stuff.

To soup this up a bit I have replaced the literals it prints with environment variables. These environment variables are defined in `.env` file as well `Dockerfile`. Both these variables are being printed.

On top of that, the `Dockerfile` also installs dependencies it gets from the `requirements.txt` file.

## What You Will Do?

- [x] Write a `Dockerfile` to convert a simple python script into an image.
- [x] Install script's dependencies while converting it to an image.
- [x] Using 2 different methods to load ENV variables inside the container.
- [x] Create a container from that image and run it to see it's output.

## How To Do It?

You will need to build your own image named `dockerize_script`. If you change this name to something else you will not be able to use the `run.sh` script.

> Make sure you are inside the `001. dockerize a simple script` folder before you attempt the following.

Build your image like this:

```shell
docker build -f ./Dockerfile --tag dockerize_script .
```

Then you need to create and run the container:

```shell
docker run --env-file .env --name dockerize_script dockerize_script
```

An easy alternative to do this is running the `run.sh` file from the terminal.

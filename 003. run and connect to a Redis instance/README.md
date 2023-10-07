# Run and connect to a Redis instance

I have established a Redis instance withing a docker container and have accessed it using a simple python script. 

I have set some values to keys and then called it back to see the response. To set another example I have set up a default counter which increases the number output by 1 each time you run the script.

## What You Will Do?

- [x] Use a pre-existing Redis image to run it in a container.
- [x] User post mapping to connect to the Redis instance from our system's environment.
- [ ] Export the cache to our system's environment.

## How To Use It?

First we need to pull a Postgres image

```shell
docker pull redis
```

Then we will create a docker container from thet image

```shell
docker run --name redis-container -d -p 6379:6379 redis
```

`-p 6379:6379` maps the port on the docker environment to our local system's environment, so we can access it on port `6379`

You can check the running container with

```shell
docker ps
```

Before you connect your python script file with the cache service instance, you need to install a driver for it.

```shell
pip install redis
```